from solders.pubkey import Pubkey

# System & pump.fun addresses
PUMP_PROGRAM = Pubkey.from_string("6EF8rrecthR5Dkzon8Nwu78hRvfCKubJ14M5uBEwF6P")
PUMP_GLOBAL = Pubkey.from_string("4wTV1YmiEkRvAtNtsSGPtUrqRYQMe5SKy2uB4Jjaxnjf")
PUMP_EVENT_AUTHORITY = Pubkey.from_string("Ce6TQqeHC9p8KetsN6JsjHK7UTZk7nasjjnr7XxXp9F1")
PUMP_FEE = Pubkey.from_string("CebN5WGQ4jvEPvsVU4EoHEpgzq1VV7AbicfhtW4xC9iM")
PUMP_LIQUIDITY_MIGRATOR = Pubkey.from_string("39azUYFWPz3VHgKCf3VChUwbpURdCHRxjWVowf5jUJjg")
SYSTEM_PROGRAM = Pubkey.from_string("11111111111111111111111111111111")
SYSTEM_TOKEN_PROGRAM = Pubkey.from_string("TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA")
SYSTEM_ASSOCIATED_TOKEN_ACCOUNT_PROGRAM = Pubkey.from_string("ATokenGPvbdGVxr1b2hvZbsiqW5xWH25efTNsLJA8knL")
SYSTEM_RENT = Pubkey.from_string("SysvarRent111111111111111111111111111111111")
SOL = Pubkey.from_string("So11111111111111111111111111111111111111112")
LAMPORTS_PER_SOL = 1_000_000_000

# Trading parameters
BUY_AMOUNT = 0.0001  # Amount of SOL to spend when buying
BUY_SLIPPAGE = 0.2  # 20% slippage tolerance for buying
SELL_SLIPPAGE = 0.2  # 20% slippage tolerance for selling

# Your nodes
# You can also get a trader node https://docs.chainstack.com/docs/solana-trader-nodes
#helius^https://mainnet.helius-rpc.com/?api-key=df9a7fb3-af4e-4d32-9922-dc1d74034154
#chainstak^https://solana-mainnet.core.chainstack.com/f11d8e197e0805aea2c47e652060950d
RPC_ENDPOINT = "https://mainnet.helius-rpc.com/?api-key=df9a7fb3-af4e-4d32-9922-dc1d74034154"
#helius^wss://mainnet.helius-rpc.com/?api-key=df9a7fb3-af4e-4d32-9922-dc1d74034154
#chainstack^wss://solana-mainnet.core.chainstack.com/f11d8e197e0805aea2c47e652060950d
WSS_ENDPOINT = "wss://mainnet.helius-rpc.com/?api-key=df9a7fb3-af4e-4d32-9922-dc1d74034154"

#Private key{bmUJcGFt.zMKpE5hl6r6Si8kwTovvM0LAPYEXE0jB}
PRIVATE_KEY = "4FNFPg1UeFFmEmS367ekEURfQZpzbbbWm8Mc9rzTgZshFTMk4AQLKt9mPTspgh68FCBkmLTZBf1tW7Lunv2tbDWR"
