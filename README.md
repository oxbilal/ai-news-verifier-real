# AI News Verifier Real

A GenLayer Intelligent Contract that uses AI non-determinism to verify claims.

## What it does

The contract accepts a user claim and asks an AI model to classify it as:

- trusted
- suspicious
- unclear

Then it stores the AI result on-chain.

## GenLayer features used

- `gl.nondet.exec_prompt`
- `gl.vm.run_nondet_unsafe`
- Validator function for JSON structure
- Public write method: `check_claim`
- Public view method: `get_last_result`

## Test claim

GenLayer uses Intelligent Contracts

## Contract address

0x8ac9f6CD1d0FE46a8E70aa871A2e545327c04975
