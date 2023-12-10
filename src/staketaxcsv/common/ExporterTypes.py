# CSV formats
FORMAT_DEFAULT = "default"
FORMAT_BALANCES = "balances"
FORMAT_ACCOINTING = "accointing"
FORMAT_AWAKENTAX = "awakentax"
FORMAT_BITCOINTAX = "bitcointax"
FORMAT_BITTYTAX = "bittytax"
FORMAT_BLOCKPIT = "blockpit"
FORMAT_COINLEDGER = "coinledger"
FORMAT_COINPANDA = "coinpanda"
FORMAT_COINTELLI = "cointelli"
FORMAT_COINTRACKING = "cointracking"
FORMAT_COINTRACKER = "cointracker"
FORMAT_CRYPTIO = "cryptio"
FORMAT_CRYPTOBOOKS = "cryptobooks"
FORMAT_CRYPTOCOM = "cryptocom"
FORMAT_CRYPTOTAXCALCULATOR = "cryptotaxcalculator"
FORMAT_CRYPTOWORTH = "cryptoworth"
FORMAT_DIVLY = "divly"
FORMAT_KOINLY = "koinly"
FORMAT_RECAP = "recap"
FORMAT_TAXBIT = "taxbit"
FORMAT_TOKENTAX = "tokentax"
FORMAT_ZENLEDGER = "zenledger"

FORMATS = [
    FORMAT_DEFAULT,
    FORMAT_BALANCES,
    FORMAT_ACCOINTING,
    FORMAT_AWAKENTAX,
    FORMAT_BITCOINTAX,
    FORMAT_BITTYTAX,
    # FORMAT_BLOCKPIT,
    FORMAT_COINLEDGER,
    FORMAT_COINPANDA,
    FORMAT_COINTELLI,
    FORMAT_COINTRACKING,
    FORMAT_COINTRACKER,
    FORMAT_CRYPTIO,
    FORMAT_CRYPTOBOOKS,
    FORMAT_CRYPTOCOM,
    FORMAT_CRYPTOTAXCALCULATOR,
    FORMAT_CRYPTOWORTH,
    FORMAT_DIVLY,
    FORMAT_KOINLY,
    FORMAT_RECAP,
    FORMAT_TAXBIT,
    FORMAT_TOKENTAX,
    FORMAT_ZENLEDGER,
]

# Other
LP_TREATMENT_TRANSFERS = "transfers"
LP_TREATMENT_OMIT = "omit"
LP_TREATMENT_TRADES = "trades"
LP_TREATMENT_CHOICES = [
    LP_TREATMENT_TRANSFERS,
    LP_TREATMENT_OMIT,
    LP_TREATMENT_TRADES
]
LP_TREATMENT_DEFAULT = LP_TREATMENT_TRANSFERS

# Note: TX_TYPE=_* means transaction is not included in non-default CSVs
# (i.e. _STAKING_DELEGATE is not included in koinly, cointracking, ... )

# ### COMMON ##########################################################################################

# Common exportable transactions
TX_TYPE_STAKING = "STAKING"  # Staking reward
TX_TYPE_AIRDROP = "AIRDROP"
TX_TYPE_TRADE = "TRADE"
TX_TYPE_TRANSFER = "TRANSFER"
TX_TYPE_SPEND = "SPEND"
TX_TYPE_INCOME = "INCOME"
TX_TYPE_BORROW = "BORROW"
TX_TYPE_REPAY = "REPAY"
TX_TYPE_LP_DEPOSIT = "LP_DEPOSIT"  # note: only koinly has export; others treat as transfer
TX_TYPE_LP_WITHDRAW = "LP_WITHDRAW"  # note: only koinly has export; others treat as transfer
TX_TYPE_MARGIN_TRADE_FEE = "MARGIN_TRADE_FEE"

# Common non-exportable transactions
TX_TYPE_UNKNOWN = "_UNKNOWN"
TX_TYPE_UNKNOWN_ERROR = "_UNKNOWN_ERROR"
TX_TYPE_EXCLUDED = "_EXCLUDED"
TX_TYPE_STAKING_DELEGATE = "_STAKING_DELEGATE"
TX_TYPE_STAKING_UNDELEGATE = "_STAKING_UNDELEGATE"
TX_TYPE_STAKING_REDELEGATE = "_STAKING_REDELEGATE"
TX_TYPE_STAKING_WITHDRAW_REWARD = "_STAKING_WITHDRAW_REWARD"
TX_TYPE_NOOP = "_NOOP"
TX_TYPE_LP_STAKE = "_LP_STAKE"
TX_TYPE_LP_UNSTAKE = "_LP_UNSTAKE"
TX_TYPE_DEPOSIT_COLLATERAL = "_DEPOSIT_COLLATERAL"
TX_TYPE_WITHDRAW_COLLATERAL = "_WITHDRAW_COLLATERAL"
TX_TYPE_STAKE = "_STAKE"
TX_TYPE_UNSTAKE = "_UNSTAKE"
TX_TYPE_FAILED_NO_FEE = "_FAILED_NO_FEE"

# ### LUNA ##########################################################################################

TX_TYPE_VOTE = "_VOTE"
TX_TYPE_GOV = "_GOV"
TX_TYPE_GOV_STAKE = "_GOV_STAKE"
TX_TYPE_GOV_UNSTAKE = "_GOV_UNSTAKE"

# mirror protocol lp
TX_TYPE_DISTRIBUTE = "_DISTRIBUTE"

# anchor earn
TX_TYPE_EARN_DEPOSIT = "_EARN_DEPOSIT"
TX_TYPE_EARN_WITHDRAW = "_EARN_WITHDRAW"

# anchor bond
TX_TYPE_BOND = "_BOND"
TX_TYPE_UNBOND = "_UNBOND"
TX_TYPE_UNBOND_WITHDRAW = "_UNBOND_WITHDRAW"
TX_TYPE_UNBOND_INSTANT = "_UNBOND_INSTANT"

# anchor liquidate
TX_TYPE_SUBMIT_BID = "_SUBMIT_BID"
TX_TYPE_RETRACT_BID = "_RETRACT_BID"

# MIR
TX_TYPE_SUBMIT_LIMIT_ORDER = "_SUBMIT_LIMIT_ORDER"

# LOTA
TX_TYPE_LOTA_UNKNOWN = "_LOTA_UNKNOWN"

# SPEC
TX_TYPE_SPEC_UNKNOWN = "_SPEC_UNKNOWN"

# ASTROPORT
TX_TYPE_ASTROPORT_UNKNOWN = "_ASTROPORT_UNKNOWN"

# MARS
TX_TYPE_MARS_UNKNOWN = "_MARS_UNKNOWN"

# VALKYRIE
TX_TYPE_VALKYRIE_UNKNOWN = "_VALKYRIE_UNKNOWN"

# nft
TX_TYPE_NFT_WHITELIST = "_NFT_WHITELIST"
TX_TYPE_NFT_MINT = "_NFT_MINT"
TX_TYPE_NFT_OFFER_SELL = "_NFT_OFFER_SELL"
TX_TYPE_NFT_OFFER_BUY = "_NFT_OFFER_BUY"
TX_TYPE_NFT_WITHDRAW = "_NFT_WITHDRAW"
TX_TYPE_NFT_DEPOSIT = "_NFT_DEPOSIT"
TX_TYPE_NFT_CANCEL_ORDER = "_NFT_CANCEL_ORDER"

# ### SOL ##########################################################################################

TX_TYPE_SOL_STAKING_SPLIT = "_STAKING_SPLIT"
TX_TYPE_SOL_STAKING_WITHDRAW = "_STAKING_WITHDRAW"
TX_TYPE_SOL_STAKING_DEACTIVATE = "_STAKING_DEACTIVATE"
TX_TYPE_SOL_STAKING_CREATE = "_STAKING_CREATE"
TX_TYPE_SOL_INIT_ACCOUNT = "_INIT_ACCOUNT"
TX_TYPE_SOL_CLOSE_ACCOUNT = "_CLOSE_ACCOUNT"
TX_TYPE_SOL_SETTLE_FUNDS = "_SETTLE_FUNDS"
TX_TYPE_MISSING_TIMESTAMP = "_ERROR"

TX_TYPE_SOL_LP_DEPOSIT = "_LP_DEPOSIT"
TX_TYPE_SOL_LP_WITHDRAW = "_LP_WITHDRAW"
TX_TYPE_SOL_LP_FARM = "_LP_FARM"
TX_TYPE_SOL_REWARD_ZERO = "_REWARD_ZERO"  # Ray staking reward 0
TX_TYPE_SOL_SERUM_DEX = "_SERUM_DEX"
TX_TYPE_SOL_TRANSFER_SELF = "_TRANSFER_SELF"
TX_TYPE_SOL_WORMHOLE_NOOP = "_WORMHOLE_NOOP"
TX_TYPE_SOL_JUPITER_OPEN_DCA = "_JUPITER_OPEN_DCA"

# ### OSMO ##########################################################################################

TX_TYPE_OSMO_VOTE = "_VOTE"
TX_TYPE_OSMO_WITHDRAW_DELEGATOR_REWARD = "_WITHDRAW_DELEGATOR_REWARD"
TX_TYPE_OSMO_WITHDRAW_COMMISSION = "_WITHDRAW_COMMISSION"
TX_TYPE_OSMO_SET_WITHDRAW_ADDRESS = "_SET_WITHDRAW_ADDRESS"
TX_TYPE_OSMO_SUBMIT_PROPOSAL = "_SUBMIT_PROPOSAL"
TX_TYPE_OSMO_DEPOSIT = "_DEPOSIT"

################################################################################################

# Types included for all CSVs (i.e. koinly, cointracking, etc).
TX_TYPES_CSVEXPORT = [
    TX_TYPE_STAKING,
    TX_TYPE_AIRDROP,
    TX_TYPE_TRADE,
    TX_TYPE_SPEND,
    TX_TYPE_INCOME,
    TX_TYPE_TRANSFER,
    TX_TYPE_BORROW,
    TX_TYPE_REPAY,
    TX_TYPE_LP_DEPOSIT,
    TX_TYPE_LP_WITHDRAW,
]

# stake.tax csv format
ROW_FIELDS = [
    "timestamp", "tx_type", "received_amount", "received_currency",
    "sent_amount", "sent_currency", "fee", "fee_currency", "comment", "txid",
    "url", "exchange", "wallet_address"
]

# fields used for unit testing
TEST_ROW_FIELDS = ["timestamp", "tx_type", "received_amount", "received_currency",
                   "sent_amount", "sent_currency", "fee", "fee_currency", "txid"]

# cointracking csv format: https://cointracking.info/import/import_csv/
CT_FIELD_TYPE = "Type"
CT_FIELD_BUY_AMOUNT = "Buy Amount"
CT_FIELD_BUY_CURRENCY = "Buy Currency"
CT_FIELD_SELL_AMOUNT = "Sell Amount"
CT_FIELD_SELL_CURRENCY = "Sell Currency"
CT_FIELD_FEE = "Fee"
CT_FIELD_FEE_CURRENCY = "Fee Currency"
CT_FIELD_EXCHANGE = "Exchange"
CT_FIELD_TRADE_GROUP = "Trade-Group"
CT_FIELD_COMMENT = "Comment"
CT_FIELD_DATE = "Date"
CT_FIELD_TXID = "Tx-ID"
CT_FIELDS = [
    CT_FIELD_TYPE, CT_FIELD_BUY_AMOUNT, CT_FIELD_BUY_CURRENCY, CT_FIELD_SELL_AMOUNT, CT_FIELD_SELL_CURRENCY,
    CT_FIELD_FEE, CT_FIELD_FEE_CURRENCY, CT_FIELD_EXCHANGE, CT_FIELD_TRADE_GROUP, CT_FIELD_COMMENT, CT_FIELD_DATE,
    CT_FIELD_TXID
]

# tokentax csv format
TT_FIELD_TYPE = "Type"
TT_FIELD_BUY_AMOUNT = "BuyAmount"
TT_FIELD_BUY_CURRENCY = "BuyCurrency"
TT_FIELD_SELL_AMOUNT = "SellAmount"
TT_FIELD_SELL_CURRENCY = "SellCurrency"
TT_FIELD_FEE_AMOUNT = "FeeAmount"
TT_FIELD_FEE_CURRENCY = "FeeCurrency"
TT_FIELD_EXCHANGE = "Exchange"
TT_FIELD_GROUP = "Group"
TT_FIELD_COMMENT = "Comment"
TT_FIELD_DATE = "Date"
TT_FIELDS = [
    TT_FIELD_TYPE,
    TT_FIELD_BUY_AMOUNT,
    TT_FIELD_BUY_CURRENCY,
    TT_FIELD_SELL_AMOUNT,
    TT_FIELD_SELL_CURRENCY,
    TT_FIELD_FEE_AMOUNT,
    TT_FIELD_FEE_CURRENCY,
    TT_FIELD_EXCHANGE,
    TT_FIELD_GROUP,
    TT_FIELD_COMMENT,
    TT_FIELD_DATE
]

# cointracker format
CR_FIELD_DATE = "Date"
CR_FIELD_RECEIVED_QUANTITY = "Received Quantity"
CR_FIELD_RECEIVED_CURRENCY = "Received Currency"
CR_FIELD_SENT_QUANTITY = "Sent Quantity"
CR_FIELD_SENT_CURRENCY = "Sent Currency"
CR_FIELD_FEE_AMOUNT = "Fee Amount"
CR_FIELD_FEE_CURRENCY = "Fee Currency"
CR_FIELD_TAG = "Tag"
CR_FIELD_TRANSACTION_ID = "Transaction ID"  # Not real field.  Added for user danb
CR_FIELDS = [
    CR_FIELD_DATE, CR_FIELD_RECEIVED_QUANTITY, CR_FIELD_RECEIVED_CURRENCY,
    CR_FIELD_SENT_QUANTITY, CR_FIELD_SENT_CURRENCY, CR_FIELD_FEE_AMOUNT,
    CR_FIELD_FEE_CURRENCY, CR_FIELD_TAG, CR_FIELD_TRANSACTION_ID
]

# coinledger format
CL_FIELD_DATE = "Date (UTC)"
CL_FIELD_PLATFORM = "Platform (Optional)"
CL_FIELD_ASSET_SENT = "Asset Sent"
CL_FIELD_AMOUNT_SENT = "Amount Sent"
CL_FIELD_ASSET_RECEIVED = "Asset Received"
CL_FIELD_AMOUNT_RECEIVED = "Amount Received"
CL_FEE_CURRENCY = "Fee Currency (Optional)"
CL_FEE_AMOUNT = "Fee Amount (Optional)"
CL_TYPE = "Type"
CL_DESCRIPTION = "Description (Optional)"
CL_TXHASH = "TxHash (Optional)"
CL_FIELDS = [
    CL_FIELD_DATE, CL_FIELD_PLATFORM, CL_FIELD_ASSET_SENT, CL_FIELD_AMOUNT_SENT, CL_FIELD_ASSET_RECEIVED,
    CL_FIELD_AMOUNT_RECEIVED, CL_FEE_CURRENCY, CL_FEE_AMOUNT, CL_TYPE, CL_DESCRIPTION, CL_TXHASH
]

# tax.crypto.com format
CRCOM_DATE = "Date"
CRCOM_TYPE = "Type"
CRCOM_RECEIVED_CURRENCY = "Received Currency"
CRCOM_RECEIVED_AMOUNT = "Received Amount"
CRCOM_RECEIVED_NET_WORTH = "Received Net Worth"
CRCOM_SENT_CURRENCY = "Sent Currency"
CRCOM_SENT_AMOUNT = "Sent Amount"
CRCOM_SENT_NET_WORTH = "Sent Net Worth"
CRCOM_FEE_CURRENCY = "Fee Currency"
CRCOM_FEE_AMOUNT = "Fee Amount"
CRCOM_FEE_NET_WORTH = "Fee Net Worth"
CRCOM_FIELDS = [
    CRCOM_DATE, CRCOM_TYPE, CRCOM_RECEIVED_CURRENCY, CRCOM_RECEIVED_AMOUNT, CRCOM_RECEIVED_NET_WORTH,
    CRCOM_SENT_CURRENCY, CRCOM_SENT_AMOUNT, CRCOM_SENT_NET_WORTH, CRCOM_FEE_CURRENCY, CRCOM_FEE_AMOUNT,
    CRCOM_FEE_NET_WORTH
]

# divly format
DIVLY_FIELD_DATE = "date"
DIVLY_FIELD_TIME = "time (UTC)"
DIVLY_FIELD_TRANSACTION_TYPE = "transaction_type"
DIVLY_FIELD_LABEL = "label"
DIVLY_FIELD_SENT_AMOUNT = "sent_amount"
DIVLY_FIELD_SENT_CURRENCY = "sent_currency"
DIVLY_FIELD_RECEIVED_AMOUNT = "received_amount"
DIVLY_FIELD_RECEIVED_CURRENCY = "received_currency"
DIVLY_FIELD_FEE_AMOUNT = "fee_amount"
DIVLY_FIELD_FEE_CURRENCY = "fee_currency"
DIVLY_FIELD_CUSTOM_DESCRIPTION = "custom_description"
DIVLY_FIELD_TX_HASH = "tx_hash"

DIVLY_FIELDS = [DIVLY_FIELD_DATE, DIVLY_FIELD_TIME, DIVLY_FIELD_TRANSACTION_TYPE, DIVLY_FIELD_LABEL,
                DIVLY_FIELD_SENT_AMOUNT, DIVLY_FIELD_SENT_CURRENCY, DIVLY_FIELD_RECEIVED_AMOUNT,
                DIVLY_FIELD_RECEIVED_CURRENCY, DIVLY_FIELD_FEE_AMOUNT, DIVLY_FIELD_FEE_CURRENCY,
                DIVLY_FIELD_CUSTOM_DESCRIPTION, DIVLY_FIELD_TX_HASH]

# cryptobooks format
CRYPTOBOOKS_FIELD_TYPE = "TYPE"
CRYPTOBOOKS_FIELD_CATEGORY = "CATEGORY"
CRYPTOBOOKS_FIELD_DATE = "TRANSACTION DATE"
CRYPTOBOOKS_FIELD_SENT_CURRENCY = "FROM CURRENCY"
CRYPTOBOOKS_FIELD_SENT_AMOUNT = "FROM AMOUNT"
CRYPTOBOOKS_FIELD_RECEIVED_CURRENCY = "TO CURRENCY"
CRYPTOBOOKS_FIELD_RECEIVED_AMOUNT = "TO AMOUNT"
CRYPTOBOOKS_FIELD_FEE_CURRENCY = "FEE CURRENCY"
CRYPTOBOOKS_FIELD_FEE_AMOUNT = "FEE AMOUNT"
CRYPTOBOOKS_FIELD_NOTES = "NOTES"
CRYPTOBOOKS_FIELD_ORIGINAL_ID = "ORIGINAL ID"

CRYPTOBOOKS_FIELDS = [
    CRYPTOBOOKS_FIELD_TYPE,
    CRYPTOBOOKS_FIELD_CATEGORY,
    CRYPTOBOOKS_FIELD_DATE,
    CRYPTOBOOKS_FIELD_SENT_CURRENCY,
    CRYPTOBOOKS_FIELD_SENT_AMOUNT,
    CRYPTOBOOKS_FIELD_RECEIVED_CURRENCY,
    CRYPTOBOOKS_FIELD_RECEIVED_AMOUNT,
    CRYPTOBOOKS_FIELD_FEE_CURRENCY,
    CRYPTOBOOKS_FIELD_FEE_AMOUNT,
    CRYPTOBOOKS_FIELD_NOTES,
    CRYPTOBOOKS_FIELD_ORIGINAL_ID
]

# koinly format
KOINLY_FIELD_DATE = "Date"
KOINLY_FIELD_SENT_AMOUNT = "Sent Amount"
KOINLY_FIELD_SENT_CURRENCY = "Sent Currency"
KOINLY_FIELD_RECEIVED_AMOUNT = "Received Amount"
KOINLY_FIELD_RECEIVED_CURRENCY = "Received Currency"
KOINLY_FIELD_FEE_AMOUNT = "Fee Amount"
KOINLY_FIELD_FEE_CURRENCY = "Fee Currency"
KOINLY_FIELD_NET_WORTH_AMOUNT = "Net Worth Amount"
KOINLY_FIELD_NET_WORTH_CURRENCY = "Net Worth Currency"
KOINLY_FIELD_LABEL = "Label"
KOINLY_FIELD_DESCRIPTION = "Description"
KOINLY_FIELD_TXHASH = "TxHash"
KOINLY_FIELDS = [
    KOINLY_FIELD_DATE,
    KOINLY_FIELD_SENT_AMOUNT,
    KOINLY_FIELD_SENT_CURRENCY,
    KOINLY_FIELD_RECEIVED_AMOUNT,
    KOINLY_FIELD_RECEIVED_CURRENCY,
    KOINLY_FIELD_FEE_AMOUNT,
    KOINLY_FIELD_FEE_CURRENCY,
    KOINLY_FIELD_NET_WORTH_AMOUNT,
    KOINLY_FIELD_NET_WORTH_CURRENCY,
    KOINLY_FIELD_LABEL,
    KOINLY_FIELD_DESCRIPTION,
    KOINLY_FIELD_TXHASH
]

# cryptotaxcalculator.io format
CALC_FIELD_TIMESTAMP = "Timestamp (UTC)"
CALC_FIELD_TYPE = "Type"
CALC_FIELD_BASE_CURRENCY = "Base Currency (Optional)"
CALC_FIELD_BASE_AMOUNT = "Base Amount (Optional)"
CALC_FIELD_QUOTE_CURRENCY = "Quote Currency (Optional)"
CALC_FIELD_QUOTE_AMOUNT = "Quote Amount (Optional)"
CALC_FIELD_FEE_CURRENCY = "Fee Currency (Optional)"
CALC_FIELD_FEE_AMOUNT = "Fee Amount (Optional)"
CALC_FIELD_FROM = "From (Optional)"
CALC_FIELD_TO = "To (Optional)"
CALC_FIELD_ID = "ID (Optional)"
CALC_FIELD_DESCRIPTION = "Description (Optional)"
CALC_FIELDS = [
    CALC_FIELD_TIMESTAMP,
    CALC_FIELD_TYPE,
    CALC_FIELD_BASE_CURRENCY,
    CALC_FIELD_BASE_AMOUNT,
    CALC_FIELD_QUOTE_CURRENCY,
    CALC_FIELD_QUOTE_AMOUNT,
    CALC_FIELD_FEE_CURRENCY,
    CALC_FIELD_FEE_AMOUNT,
    CALC_FIELD_FROM,
    CALC_FIELD_TO,
    CALC_FIELD_ID,
    CALC_FIELD_DESCRIPTION
]

# accointing .xlsl fields
ACCOINT_FIELD_TRANSACTION_TYPE = "transactionType"
ACCOINT_FIELD_DATE = "date"
ACCOINT_FIELD_IN_BUY_AMOUNT = "inBuyAmount"
ACCOINT_FIELD_IN_BUY_ASSET = "inBuyAsset"
ACCOINT_FIELD_OUT_SELL_AMOUNT = "outSellAmount"
ACCOINT_FIELD_OUT_SELL_ASSET = "outSellAsset"
ACCOINT_FIELD_FEE_AMOUNT = "feeAmount (optional)"
ACCOINT_FIELD_FEE_ASSET = "feeAsset (optional)"
ACCOINT_FIELD_CLASSIFICATION = "classification (optional)"
ACCOINT_FIELD_OPERATION_ID = "operationId (optional)"
ACCOINT_FIELD_COMMENTS = "comments (optional)"
ACCOINT_FIELDS = [
    ACCOINT_FIELD_TRANSACTION_TYPE,
    ACCOINT_FIELD_DATE,
    ACCOINT_FIELD_IN_BUY_AMOUNT,
    ACCOINT_FIELD_IN_BUY_ASSET,
    ACCOINT_FIELD_OUT_SELL_AMOUNT,
    ACCOINT_FIELD_OUT_SELL_ASSET,
    ACCOINT_FIELD_FEE_AMOUNT,
    ACCOINT_FIELD_FEE_ASSET,
    ACCOINT_FIELD_CLASSIFICATION,
    ACCOINT_FIELD_OPERATION_ID,
    ACCOINT_FIELD_COMMENTS,
]

# zenledger fields
ZEN_FIELD_TIMESTAMP = "Timestamp"
ZEN_FIELD_TYPE = "Type"
ZEN_FIELD_IN_AMOUNT = "IN Amount"
ZEN_FIELD_IN_CURRENCY = "IN Currency"
ZEN_FIELD_OUT_AMOUNT = "Out Amount"
ZEN_FIELD_OUT_CURRENCY = "Out Currency"
ZEN_FIELD_FEE_AMOUNT = "Fee Amount"
ZEN_FIELD_FEE_CURRENCY = "Fee Currency"
ZEN_FIELD_EXCHANGE = "Exchange(optional)"
ZEN_FIELD_US_BASED = "US Based"
ZEN_FIELDS = [
    ZEN_FIELD_TIMESTAMP,
    ZEN_FIELD_TYPE,
    ZEN_FIELD_IN_AMOUNT,
    ZEN_FIELD_IN_CURRENCY,
    ZEN_FIELD_OUT_AMOUNT,
    ZEN_FIELD_OUT_CURRENCY,
    ZEN_FIELD_FEE_AMOUNT,
    ZEN_FIELD_FEE_CURRENCY,
    ZEN_FIELD_EXCHANGE,
    ZEN_FIELD_US_BASED
]

# taxbit fields
TAXBIT_FIELD_DATE_AND_TIME = "Date and Time"
TAXBIT_FIELD_TRANSACTION_TYPE = "Transaction Type"
TAXBIT_FIELD_SENT_QUANTITY = "Sent Quantity"
TAXBIT_FIELD_SENT_CURRENCY = "Sent Currency"
TAXBIT_FIELD_SENDING_SOURCE = "Sending Source"
TAXBIT_FIELD_RECEIVED_QUANTITY = "Received Quantity"
TAXBIT_FIELD_RECEIVED_CURRENCY = "Received Currency"
TAXBIT_FIELD_RECEIVING_DESTINATION = "Receiving Destination"
TAXBIT_FIELD_FEE = "Fee"
TAXBIT_FIELD_FEE_CURRENCY = "Fee Currency"
TAXBIT_FIELD_EXCHANGE_TRANSACTION_ID = "Exchange Transaction ID"
TAXBIT_FIELD_BLOCKCHAIN_TRANSACTION_HASH = "Blockchain Transaction Hash"
TAXBIT_FIELDS = [
    TAXBIT_FIELD_DATE_AND_TIME,
    TAXBIT_FIELD_TRANSACTION_TYPE,
    TAXBIT_FIELD_SENT_QUANTITY,
    TAXBIT_FIELD_SENT_CURRENCY,
    TAXBIT_FIELD_SENDING_SOURCE,
    TAXBIT_FIELD_RECEIVED_QUANTITY,
    TAXBIT_FIELD_RECEIVED_CURRENCY,
    TAXBIT_FIELD_RECEIVING_DESTINATION,
    TAXBIT_FIELD_FEE,
    TAXBIT_FIELD_FEE_CURRENCY,
    TAXBIT_FIELD_EXCHANGE_TRANSACTION_ID,
    TAXBIT_FIELD_BLOCKCHAIN_TRANSACTION_HASH
]

# recap format
RECAP_FIELD_TYPE = "Type"
RECAP_FIELD_DATE = "Date"
RECAP_FIELD_INORBUYAMOUNT = "InOrBuyAmount"
RECAP_FIELD_INORBUYCURRENCY = "InOrBuyCurrency"
RECAP_FIELD_OUTORSELLAMOUNT = "OutOrSellAmount"
RECAP_FIELD_OUTORSELLCURRENCY = "OutOrSellCurrency"
RECAP_FIELD_FEEAMOUNT = "FeeAmount"
RECAP_FIELD_FEECURRENCY = "FeeCurrency"
RECAP_FIELD_DESCRIPTION = "Description"  # Not an importable field.
RECAP_FIELD_TXID = "Transaction ID"  # Not an importable field.
RECAP_FIELDS = [
    RECAP_FIELD_TYPE,
    RECAP_FIELD_DATE,
    RECAP_FIELD_INORBUYAMOUNT,
    RECAP_FIELD_INORBUYCURRENCY,
    RECAP_FIELD_OUTORSELLAMOUNT,
    RECAP_FIELD_OUTORSELLCURRENCY,
    RECAP_FIELD_FEEAMOUNT,
    RECAP_FIELD_FEECURRENCY,
    RECAP_FIELD_DESCRIPTION,
    RECAP_FIELD_TXID
]

# bitcoin.tax format
BTAX_FIELD_DATE = "Date"
BTAX_FIELD_ACTION = "Action"
BTAX_FIELD_SYMBOL = "Symbol"
BTAX_FIELD_VOLUME = "Volume"
BTAX_FIELD_CURRENCY = "Currency"
BTAX_FIELD_TOTAL = "Total"
BTAX_FIELD_FEE = "Fee"
BTAX_FIELD_FEE_CURRENCY = "FeeCurrency"
BTAX_FIELD_MEMO = "Memo"

BTAX_FIELDS = [
    BTAX_FIELD_DATE,
    BTAX_FIELD_ACTION,
    BTAX_FIELD_SYMBOL,
    BTAX_FIELD_VOLUME,
    BTAX_FIELD_CURRENCY,
    BTAX_FIELD_TOTAL,
    BTAX_FIELD_FEE,
    BTAX_FIELD_FEE_CURRENCY,
    BTAX_FIELD_MEMO,
]

# coinpanda format
CP_FIELD_TIMESTAMP = "Timestamp (UTC)"
CP_FIELD_TYPE = "Type"
CP_FIELD_SENT_AMOUNT = "Sent Amount"
CP_FIELD_SENT_CURRENCY = "Sent Currency"
CP_FIELD_RECEIVED_AMOUNT = "Received Amount"
CP_FIELD_RECEIVED_CURRENCY = "Received Currency"
CP_FIELD_FEE_AMOUNT = "Fee Amount"
CP_FIELD_FEE_CURRENCY = "Fee Currency"
CP_FIELD_NET_WORTH_AMOUNT = "Net Worth Amount"
CP_FIELD_NET_WORTH_CURRENCY = "Net Worth Currency"
CP_FIELD_LABEL = "Label"
CP_FIELD_DESCRIPTION = "Description"
CP_FIELD_TXHASH = "TxHash"

CP_FIELDS = [
    CP_FIELD_TIMESTAMP,
    CP_FIELD_TYPE,
    CP_FIELD_SENT_AMOUNT,
    CP_FIELD_SENT_CURRENCY,
    CP_FIELD_RECEIVED_AMOUNT,
    CP_FIELD_RECEIVED_CURRENCY,
    CP_FIELD_FEE_AMOUNT,
    CP_FIELD_FEE_CURRENCY,
    CP_FIELD_NET_WORTH_AMOUNT,
    CP_FIELD_NET_WORTH_CURRENCY,
    CP_FIELD_LABEL,
    CP_FIELD_DESCRIPTION,
    CP_FIELD_TXHASH,
]

# cointelli format
COINTELLI_FIELD_TIMESTAMP = "Timestamp"
COINTELLI_FIELD_TYPE = "Type"
COINTELLI_FIELD_OUT_CURRENCY = "Out Currency"
COINTELLI_FIELD_OUT_QUANTITY = "Out Quantity"
COINTELLI_FIELD_IN_CURRENCY = "In Currency"
COINTELLI_FIELD_IN_QUANTITY = "In Quantity"
COINTELLI_FIELD_FEE_CURRENCY = "Fee Currency"
COINTELLI_FIELD_FEE_QUANTITY = "Fee Quantity"
COINTELLI_FIELD_COMMENTS = "Comments"

COINTELLI_FIELDS = [
    COINTELLI_FIELD_TIMESTAMP,
    COINTELLI_FIELD_TYPE,
    COINTELLI_FIELD_OUT_CURRENCY,
    COINTELLI_FIELD_OUT_QUANTITY,
    COINTELLI_FIELD_IN_CURRENCY,
    COINTELLI_FIELD_IN_QUANTITY,
    COINTELLI_FIELD_FEE_CURRENCY,
    COINTELLI_FIELD_FEE_QUANTITY,
    COINTELLI_FIELD_COMMENTS,
]

# blockpit format
BLOCKPIT_FIELD_ID = "id"
BLOCKPIT_FIELD_EXCHANGE_NAME = "exchange_name"
BLOCKPIT_FIELD_DEPOT_NAME = "depot_name"
BLOCKPIT_FIELD_TRANSACTION_DATE = "transaction_date"
BLOCKPIT_FIELD_BUY_ASSET = "buy_asset"
BLOCKPIT_FIELD_BUY_AMOUNT = "buy_amount"
BLOCKPIT_FIELD_SELL_ASSET = "sell_asset"
BLOCKPIT_FIELD_SELL_AMOUNT = "sell_amount"
BLOCKPIT_FIELD_FEE_ASSET = "fee_asset"
BLOCKPIT_FIELD_FEE_AMOUNT = "fee_amount"
BLOCKPIT_FIELD_TRANSACTION_TYPE = "transaction_type"

BLOCKPIT_FIELDS = [
    BLOCKPIT_FIELD_ID,
    BLOCKPIT_FIELD_EXCHANGE_NAME,
    BLOCKPIT_FIELD_DEPOT_NAME,
    BLOCKPIT_FIELD_TRANSACTION_DATE,
    BLOCKPIT_FIELD_BUY_ASSET,
    BLOCKPIT_FIELD_BUY_AMOUNT,
    BLOCKPIT_FIELD_SELL_ASSET,
    BLOCKPIT_FIELD_SELL_AMOUNT,
    BLOCKPIT_FIELD_FEE_ASSET,
    BLOCKPIT_FIELD_FEE_AMOUNT,
    BLOCKPIT_FIELD_TRANSACTION_TYPE,
]

# cryptio format
CRYPTIO_FIELD_TRANSACTION_DATE = "transactionDate"
CRYPTIO_FIELD_ORDER_TYPE = "orderType"
CRYPTIO_FIELD_TXHASH = "txhash"
CRYPTIO_FIELD_INCOMING_ASSET = "incomingAsset"
CRYPTIO_FIELD_INCOMING_VOLUME = "incomingVolume"
CRYPTIO_FIELD_OUTGOING_ASSET = "outgoingAsset"
CRYPTIO_FIELD_OUTGOING_VOLUME = "outgoingVolume"
CRYPTIO_FIELD_FEE_ASSET = "feeAsset"
CRYPTIO_FIELD_FEE_VOLUME = "feeVolume"
CRYPTIO_FIELD_OTHER_PARTIES = "otherParties"
CRYPTIO_FIELD_NOTE = "note"
CRYPTIO_FIELD_SUCCESS = "success"
CRYPTIO_FIELD_INTERNAL_TRANSFER = "internalTransfer"

CRYPTIO_FIELDS = [
    CRYPTIO_FIELD_TRANSACTION_DATE,
    CRYPTIO_FIELD_ORDER_TYPE,
    CRYPTIO_FIELD_TXHASH,
    CRYPTIO_FIELD_INCOMING_ASSET,
    CRYPTIO_FIELD_INCOMING_VOLUME,
    CRYPTIO_FIELD_OUTGOING_ASSET,
    CRYPTIO_FIELD_OUTGOING_VOLUME,
    CRYPTIO_FIELD_FEE_ASSET,
    CRYPTIO_FIELD_FEE_VOLUME,
    CRYPTIO_FIELD_OTHER_PARTIES,
    CRYPTIO_FIELD_NOTE,
    CRYPTIO_FIELD_SUCCESS,
    CRYPTIO_FIELD_INTERNAL_TRANSFER,
]

# bittytax format
BITTYTAX_FIELD_TYPE = "Type"
BITTYTAX_FIELD_BUY_QUANTITY = "Buy Quantity"
BITTYTAX_FIELD_BUY_ASSET = "Buy Asset"
BITTYTAX_FIELD_BUY_VALUE = "Buy Value"
BITTYTAX_FIELD_SELL_QUANTITY = "Sell Quantity"
BITTYTAX_FIELD_SELL_ASSET = "Sell Asset"
BITTYTAX_FIELD_SELL_VALUE = "Sell Value"
BITTYTAX_FIELD_FEE_QUANTITY = "Fee Quantity"
BITTYTAX_FIELD_FEE_ASSET = "Fee Asset"
BITTYTAX_FIELD_FEE_VALUE = "Fee Value"
BITTYTAX_FIELD_WALLET = "Wallet"
BITTYTAX_FIELD_TIMESTAMP = "Timestamp"
BITTYTAX_FIELD_NOTE = "Note"
BITTYTAX_FIELD_EXCHANGE = "Exchange"
BITTYTAX_FIELD_WALLET_ADDRESS = "Wallet Address"
BITTYTAX_FIELD_TX_ID = "Tx ID"
BITTYTAX_FIELD_URL = "URL"
BITTYTAX_FIELD_RAW = "Raw Data"

BITTYTAX_FIELDS = [
    BITTYTAX_FIELD_TYPE,
    BITTYTAX_FIELD_BUY_QUANTITY,
    BITTYTAX_FIELD_BUY_ASSET,
    BITTYTAX_FIELD_BUY_VALUE,
    BITTYTAX_FIELD_SELL_QUANTITY,
    BITTYTAX_FIELD_SELL_ASSET,
    BITTYTAX_FIELD_SELL_VALUE,
    BITTYTAX_FIELD_FEE_QUANTITY,
    BITTYTAX_FIELD_FEE_ASSET,
    BITTYTAX_FIELD_FEE_VALUE,
    BITTYTAX_FIELD_WALLET,
    BITTYTAX_FIELD_TIMESTAMP,
    BITTYTAX_FIELD_NOTE,
    BITTYTAX_FIELD_TX_ID,
    BITTYTAX_FIELD_URL,
    BITTYTAX_FIELD_RAW,
]
