// Copyright ©, 2023, Lightspark Group, Inc. - All Rights Reserved

use base64::Engine;
use bitcoin::consensus::{serialize, Encodable};
use bitcoin::psbt::Psbt;
use bitcoin::secp256k1::ecdsa::Signature;
use bitcoin::util::sighash;
use bitcoin::{consensus::Decodable, psbt::PartiallySignedTransaction};
use bitcoin::{Address, EcdsaSighashType, Script, Sighash, Witness};
use pyo3::{pyclass, pymethods};
use pyo3::{PyCell, PyResult};

/// Helper struct to be used with Bitcoin functions, since internal structs are not exposed to Python.
#[pyclass]
#[derive(Clone)]
pub struct Tx {
    pub psbt: Psbt,
}

#[pymethods]
impl Tx {
    fn __repr__(slf: &PyCell<Self>) -> PyResult<String> {
        // This is the equivalent of `self.__class__.__name__` in Python.
        let class_name: &str = slf.get_type().name()?;
        // To access fields of the Rust struct, we need to borrow the `PyCell`.
        Ok(format!(
            "{}({})",
            class_name,
            slf.borrow().psbt.unsigned_tx.txid()
        ))
    }

    fn serialize_psbt(&self) -> PyResult<String> {
        let mut psbt_consensus_encoded = vec![];
        self.psbt.consensus_encode(&mut psbt_consensus_encoded)?;

        Ok(base64::engine::general_purpose::STANDARD.encode(&psbt_consensus_encoded))
    }
}

/// Generates [Tx] from consensus encoded PSBT, updates it with a desired output address and offsets the output to include some constant fee.
pub fn psbt_bytes_to_tx(psbt: Vec<u8>, address: String, fee_offset_sat: u64) -> anyhow::Result<Tx> {
    let mut psbt = PartiallySignedTransaction::consensus_decode(&mut &psbt[..])?;
    let address: Address = address.parse()?;
    psbt.unsigned_tx.output[0].script_pubkey = address.payload.script_pubkey();
    psbt.unsigned_tx.output[0].value = psbt.unsigned_tx.output[0].value - fee_offset_sat;

    Ok(Tx { psbt })
}

/// Generate Sighash for signing from a PSBT input at position input_idx to be used in a witness script.
/// Requires the witness script and the amount of the input.
/// Sighash has to be calculated in Sparkcore, because this is where we update the transaction's output address and adjust the fee.
/// The input scripts are not signed and not a part of the sighash.
pub fn generate_sighash(
    psbt: Psbt,
    input_idx: usize,
    witness_script: Vec<u8>,
    amount_sats: u64,
) -> anyhow::Result<Sighash> {
    let witness_script = Script::from(witness_script);
    let sighash = sighash::SighashCache::new(&psbt.unsigned_tx).segwit_signature_hash(
        input_idx,
        &witness_script,
        amount_sats,
        EcdsaSighashType::All,
    )?;

    Ok(sighash)
}

/// Generates signed Bitcoin Transaction from PSBT using redeem scripts and signatures, then serializes it to raw bytes.
/// List of signatures and redeem scripts is used to construct witness scripts.
/// The resulting bytes can be hex encoded to broadcast using bitcoin-cli:
/// ```
/// RUN_BTC_CLI decoderawtransaction "0200000000010104ef6bc59e69fe2c23805d80061c1e2bcf157d734d9b74a1f22bafb8e972952200000000009000000001141e0000000000001600146ca4a629f18d3346ed3aaf79e453d491ad92966e03483045022100dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd3007802200d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d3501004d632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac00000000"
/// ```
pub fn signed_serialized_tx(
    mut tx: Tx,
    signatures: Vec<Vec<u8>>,
    scripts: Vec<Vec<u8>>,
) -> anyhow::Result<Vec<u8>> {
    let r = signatures
        .into_iter()
        .zip(scripts.into_iter())
        .enumerate()
        .map(|(input_idx, (signature, script))| (input_idx, gen_witness(&signature, &script)));
    for (input_idx, wit_res) in r {
        tx.psbt.inputs[input_idx].final_script_witness = Some(wit_res?);
    }
    Ok(serialize(&tx.psbt.extract_tx()))
}

fn gen_witness(signature: &Vec<u8>, script: &Vec<u8>) -> anyhow::Result<Witness> {
    let local_delayedsig = Signature::from_compact(&signature)?;
    let mut witness_vec = Vec::with_capacity(3);
    witness_vec.push(local_delayedsig.serialize_der().to_vec());
    witness_vec[0].push(EcdsaSighashType::All as u8);
    witness_vec.push(vec![]);
    witness_vec.push(script.clone());
    Ok(Witness::from_vec(witness_vec))
}

#[cfg(test)]
mod test {

    use super::*;
    use base64::engine::general_purpose;
    use bitcoin::{consensus::deserialize, Network, Transaction};

    #[test]
    fn test_serialized_transaction_from_psbt() {
        let tx = psbt_bytes_to_tx(general_purpose::STANDARD.decode("cHNidP8BAD0CAAAAAQTva8Weaf4sI4BdgAYcHivPFX1zTZt0ofIrr7jpcpUiAAAAAACQAAAAAdweAAAAAAAAAWoAAAAAAAEBK0AfAAAAAAAAIgAgXf3xfjEkzIErgLE6DfYEPSRbFIKLTUOeNcEaNr8oa4YBCJkDSDBFAiEAqtqw/yUfYQ2homChjBlTVk0RirKs3bVTJyQE+ZiRXqQCIEK4vf3N9ct88b0CZE47J7ILuHBZOwSt30k/hK8CRq1DAQBNYyEC33htlXV7FeMaX2AyF2+JEjEsm7pq8aTY3c+3VhrMevVnApAAsnUhA2C+RAkpcAQgXmvfcmuD7GxWDE0KalsapUVTbOBTaFSVaKwAAA==").expect("psbt base64"), "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string(), 0).expect("psbt");
        assert_eq!(
            format!(
                "{}",
                Address::from_script(
                    &tx.psbt.unsigned_tx.output[0].script_pubkey,
                    Network::Regtest
                )
                .unwrap()
            ),
            "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string()
        );

        let _sighash = generate_sighash(tx.psbt.clone(), 0, hex::decode("632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac").expect("hex"),
        8000).expect("sighash");

        let tx_ser = signed_serialized_tx(tx, vec![hex::decode("dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd300780d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d35").expect("bytes")], vec![hex::decode("632102df786d95757b15e31a5f6032176f8912312c9bba6af1a4d8ddcfb7561acc7af567029000b275210360be4409297004205e6bdf726b83ec6c560c4d0a6a5b1aa545536ce05368549568ac").expect("hex")]);
        let tx: Transaction = deserialize(tx_ser.unwrap().as_slice()).unwrap();
        // signature der format is 71 bytes
        assert_eq!(hex::encode(tx.input[0].witness.to_vec()[0].as_slice()), "3045022100dd8714e2e3673e64a941d37ad5b71fa22f0706cea444c7083fefe9abbfd3007802200d67d4f2b71601bcd6ba064c42876e0302496d67b96fd351a7f2136569042d3501");
    }

    #[test]
    fn test_sighash() {
        /*
        {
            "txid": "14e10e80c42e72c464fd5bd590601cdcb4cb1908c79fccd8074a1b70bdd8c1b0",
            "hash": "14e10e80c42e72c464fd5bd590601cdcb4cb1908c79fccd8074a1b70bdd8c1b0",
            "version": 2,
            "size": 82,
            "vsize": 82,
            "weight": 328,
            "locktime": 0,
            "vin": [
                {
                "txid": "45051f45f8267d1ca2703405db0e3fea5789e3fdef35a3563c2e02340d3293e7",
                "vout": 0,
                "scriptSig": {
                    "asm": "",
                    "hex": ""
                },
                "sequence": 144
                }
            ],
            "vout": [
                {
                "value": 0.00000801,
                "n": 0,
                "scriptPubKey": {
                    "asm": "0 6ca4a629f18d3346ed3aaf79e453d491ad92966e",
                    "desc": "addr(bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek)#w9srlrnf",
                    "hex": "00146ca4a629f18d3346ed3aaf79e453d491ad92966e",
                    "address": "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek", <<<<<<<<<<<<<<<<<<
                    "type": "witness_v0_keyhash"
                }
                }
            ]
            }

            {
                "txid": "3dd827778fd268da51a52c9241aaadd3f976a340b670d196a3a353fdf4c57203",
                "hash": "ef59be4dc5fa852a9b6ced993edb8bacf29050f8bf480f6dc3d1bcf050ca8b95",
                "version": 2,
                "size": 236,
                "vsize": 121,
                "weight": 482,
                "locktime": 0,
                "vin": [
                    {
                    "txid": "45051f45f8267d1ca2703405db0e3fea5789e3fdef35a3563c2e02340d3293e7",
                    "vout": 0,
                    "scriptSig": {
                        "asm": "",
                        "hex": ""
                    },
                    "txinwitness": [
                        "3044022059c62fa242811eafbe7a3bca8267b0f347cda6383b917aaa190f075ee7ce45a70220527457f23bad4b418d421b5a299724349ed6b28da52386f8b2221aa966c3633201",
                        "",
                        "63210268767b443120eb4eb2d4f8b6c61efdfa5246a2cccf4dd7e686fc93d0b5a328e267029000b2752102dfff4f18c3704ff2eea7ffca487a63f61a02f4ad9898f5e13ce6953b9f646b8a68ac"
                    ],
                    "sequence": 144
                    }
                ],
                "vout": [
                    {
                    "value": 0.00000801,
                    "n": 0,
                    "scriptPubKey": {
                        "asm": "0 6b0009af85b18052eb83afbdc9c45521c552588f",
                        "desc": "addr(bcrt1qdvqqntu9kxq996ur477un3z4y8z4yky0ex3yye)#sd3ceqsj",
                        "hex": "00146b0009af85b18052eb83afbdc9c45521c552588f",
                        "address": "bcrt1qdvqqntu9kxq996ur477un3z4y8z4yky0ex3yye",
                        "type": "witness_v0_keyhash"
                    }
                    }
                ]
            }

         */
        let tx = psbt_bytes_to_tx(general_purpose::STANDARD.decode("cHNidP8BAD0CAAAAAeeTMg00Ai48VqM17/3jiVfqPw7bBTRwohx9JvhFHwVFAAAAAACQAAAAASEDAAAAAAAAAWoAAAAAAAEBK+gDAAAAAAAAIgAg6jOgycpx+Ms8egAs4LKJuHtm99yktHSAKHV9zNSajEUAAA==").expect("psbt base64"), "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string(), 0).expect("psbt");
        println!("{:?}", hex::encode(serialize(&tx.psbt.extract_tx())));

        let psbtb = hex::decode("70736274ff01003d0200000001e793320d34022e3c56a335effde38957ea3f0edb053470a21c7d26f8451f0545000000000090000000012103000000000000016a000000000001012be803000000000000220020ea33a0c9ca71f8cb3c7a002ce0b289b87b66f7dca4b4748028757dccd49a8c450000").expect("bytes");
        let tx = psbt_bytes_to_tx(
            psbtb,
            "bcrt1qdjj2v20335e5dmf64au7g575jxke99nwg04fek".to_string(),
            0,
        )
        .expect("psbt");

        println!("{:?}", hex::encode(serialize(&tx.psbt.extract_tx())));

        // "0200000001e793320d34022e3c56a335effde38957ea3f0edb053470a21c7d26f8451f05450000000000900000000121030000000000001600146ca4a629f18d3346ed3aaf79e453d491ad92966e00000000"
        // "0200000001e793320d34022e3c56a335effde38957ea3f0edb053470a21c7d26f8451f05450000000000900000000121030000000000001600146ca4a629f18d3346ed3aaf79e453d491ad92966e00000000"

        // -[ RECORD 1 ]-------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        // signable_id         | 018bcb72-5552-4954-0000-3c7c3a4a432e
        // payload_index       | 0
        // payload             | \x6e274641733e07291feab09c5fe7cf620b4fd415740b7cb1da90eb0d26297f37
        // derivation_path     | m/3/1156486256/3
        // status              | SIGNED
        // add_tweak           |
        // mul_tweak           |
        // signature           | \x59c62fa242811eafbe7a3bca8267b0f347cda6383b917aaa190f075ee7ce45a7527457f23bad4b418d421b5a299724349ed6b28da52386f8b2221aa966c36332
        // bitcoin_transaction | \x70736274ff01003d0200000001e793320d34022e3c56a335effde38957ea3f0edb053470a21c7d26f8451f0545000000000090000000012103000000000000016a000000000001012be803000000000000220020ea33a0c9ca71f8cb3c7a002ce0b289b87b66f7dca4b4748028757dccd49a8c450000
        // script              | \x63210268767b443120eb4eb2d4f8b6c61efdfa5246a2cccf4dd7e686fc93d0b5a328e267029000b2752102dfff4f18c3704ff2eea7ffca487a63f61a02f4ad9898f5e13ce6953b9f646b8a68ac
        // amount_sats         | 1000
        // id                  | 018bcb72-5556-c95c-0000-b18325b2a3f6
        // is_soft_deleted     | f
        // created_at          | 2023-11-14 01:29:09.71844+00
        // updated_at          | 2023-11-14 01:30:11.126624+00

        assert!(false)
    }
}
