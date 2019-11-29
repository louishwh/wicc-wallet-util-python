#!/usr/bin/python

from wicc.wallet import Wallet
from wicc.transactions import *
from wicc.baas.manager import BaasManager

# import re
# def mySplit2(str):
#     t = str.upper()
#     p = re.compile('.{1,2}')  # 匹配任意字符1-2次
#     list = [int(x, 16)  for x in p.findall(t)]
#     new = []
#     for i in list:
#         if i > 128:
#             new.append(i-256)
#         else:
#             new.append(i)
#     print(new)
#     print("长度{}".format(len(new)))

if __name__ == '__main__':
    # - 维基币地址生成 (Key and address generation)
    # # 资产发布
    # print(Wallet.generate_private_key(main_net=False))
    # import os
    # print(Wallet.generate_private_key(main_net=True))
    # print(os.path.join(os.path.dirname(os.path.realpath(__file__))))
    #
    # print(Wallet("PjkPUiuHDatebfRTT9KiuKt4pWeBw6MQDchyPQiukpXD8w8KioxW", main_net=True).wallet_address)
    #
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    # tr = AssetPublishTransaction()
    # tr.valid_height = 11443
    # tr.fee_amount = 1000000
    # tr.register_id = "0-1"
    # tr.fee_coin_symbol = CoinType.WICC.value
    # tr.asset_update_type = AssetUpdateType.OWNER_UID.value
    # tr.asset_update_value = "0-2"
    # tr.asset_symbol = "STOOOOO"
    # raw_tx = wallet.asset_publish_tx(tr)
    # print(raw_tx)
    #
    # # cdp：创建/追加
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    #
    # tr = CdpStakeTransaction()
    # tr.valid_height = 5003
    # tr.fee_amount = 10000000
    # tr.register_id = "0-1"
    # tr.fee_coin_symbol = CoinType.WUSD.value
    # tr.stake_list = [CdpStakeAsset(CoinType.WICC.value, 100000000)]
    # tr.cdp_id = "009c0e665acdd9e8ae754f9a51337b85bb8996980a93d6175b61edccd3cdc144"
    # tr.get_coin_symbol = CoinType.WUSD.value
    # tr.get_amount = 50000000
    # raw_tx = wallet.cdp_stake_tx(tr)
    # print(raw_tx)
    #
    # # 赎回cdp交易
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    #
    # tr = CdpRedeemTransaction()
    # tr.valid_height = 8510
    # tr.register_id = "0-1"
    # tr.fee_amount = 10000000
    # tr.fee_coin_symbol = CoinType.WICC.value
    # tr.redeem_list = [CdpRedeemAsset(CoinType.WICC.value, 100000000)]
    # tr.cdp_id = "009c0e665acdd9e8ae754f9a51337b85bb8996980a93d6175b61edccd3cdc144"
    # tr.repay_amount = 50000000
    # raw_tx = wallet.cdp_redeem_tx(tr)
    # print(raw_tx)
    #
    # # 清算cdp交易
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    #
    # tr = CdpLiquidateTransaction()
    # tr.valid_height = 283308
    # tr.register_id = "0-1"
    # tr.fee_amount = 10000000
    # tr.fee_coin_symbol = CoinType.WICC.value
    # tr.cdp_id = "009c0e665acdd9e8ae754f9a51337b85bb8996980a93d6175b61edccd3cdc144"
    # tr.liquidate_amount = 10000000
    # tr.liquidate_coin_symbol = CoinType.WICC.value
    # raw_tx = wallet.cdp_liquidate_tx(tr)
    # print(raw_tx)

    # dex限价买单
    wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")

    tr = DexLimitedPriceBuyTransaction()
    tr.fee_amount = 10000000
    tr.fee_coin_symbol = CoinType.WICC.value
    tr.valid_height = 283308
    tr.register_id = "0-1"
    tr.coin_symbol = CoinType.WUSD.value
    tr.asset_symbol = CoinType.WICC.value
    tr.asset_amount = 100 * 100000000
    tr.price = 10 * 10000
    rawtx = wallet.dex_limited_price_buy_tx(tr)
    print(rawtx)

    # dex限价卖单
    wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    tr = DexLimitedPriceSellTransaction()
    tr.fee_amount = 10000000
    tr.fee_coin_symbol = CoinType.WICC.value
    tr.valid_height = 283308
    tr.register_id = "0-1"
    tr.coin_symbol = CoinType.WUSD.value
    tr.asset_symbol = CoinType.WICC.value
    tr.asset_amount = 100 * 100000000
    tr.price = 1 * 10000
    rawtx = wallet.dex_limited_price_sell_tx(tr)
    print(rawtx)

    # dex市价买单
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    # tr = DexMarketPriceBuyTransaction()
    # tr.fee_amount = 10000000
    # tr.fee_coin_symbol = CoinType.WICC.value
    # tr.valid_height = 283308
    # tr.register_id = "0-1"
    # tr.coin_symbol = CoinType.WUSD.value
    # tr.coin_amount = 100 * 100000000
    # tr.asset_symbol = CoinType.WICC.value
    # rawtx = wallet.dex_market_price_buy_tx(tr)
    # print(rawtx)

    # dex市价卖单
    # wallet = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    # tr = DexMarketPriceSellTransaction()
    # tr.fee_amount = 10000000
    # tr.fee_coin_symbol = CoinType.WICC.value
    # tr.valid_height = 283308
    # tr.register_id = "0-1"
    # tr.coin_symbol = CoinType.WUSD.value
    # tr.asset_symbol = CoinType.WICC.value
    # tr.asset_amount = 100 * 100000000
    # rawtx = wallet.dex_market_price_sell_tx(tr)
    # print(rawtx)

    # dex取消订单
    wallet = Wallet("Y9XMqNzseQFSK32SvMDNF9J7xz1CQmHRsmY1hMYiqZyTck8pYae3")
    tr = DexCancelOrderTransaction()
    tr.fee_amount = 1000000
    tr.fee_coin_symbol = CoinType.WICC.value
    tr.valid_height = 283308
    tr.register_id = "0-1"
    tr.order_id = "009c0e665acdd9e8ae754f9a51337b85bb8996980a93d6175b61edccd3cdc144"
    rawtx = wallet.dex_cancel_order_tx(tr)
    print(rawtx)

    # 转账交易
    w = Wallet("Y5NyUyMeRkVX18WUB7ybwjuN8wruTi7HJpdPbFKnRBqKPQ215SpV")
    tr = TransferTransaction()
    tr.valid_height = BaasManager.get_valid_height()
    tr.register_id = "265866-2"
    tr.fee_amount = 10000000
    tr.fee_coin_symbol = "WICC"
    tr.memo = "转账"
    tr.transfer_list = [
        Transfer(amount=10000000000, symbol="WICC", desert_address="wahso3aWQFtFpmaTmFF8FFYbiM88xE4R4h"),
        Transfer(amount=10000000000, symbol="WICC", desert_address="wMS4ZG4xfoTY9MXpbykTPvFPzFViPa6aGf"),
    ]
    rawtx = w.transfer_tx(tr)
    print(BaasManager.submit_tx(rawtx))

    # 合约调用
    w = Wallet("Y6J4aK6Wcs4A3Ex4HXdfjJ6ZsHpNZfjaS4B9w7xqEnmFEYMqQd13")
    contract_call = ContractCallTransaction()
    contract_call.valid_height = BaasManager.get_valid_height()
    contract_call.register_id = "0-1"
    contract_call.fee_amount = 100000
    contract_call.fee_coin_symbol = CoinType.WICC.value
    contract_call.app_id = "450687-1"
    contract_call.contract_call_msg = "f001"
    contract_call.pay_coin_symbol = CoinType.WUSD.value
    contract_call.pay_amount = 100000000
    contract_call_rawtx = w.contract_call_tx(contract_call)
    print(contract_call_rawtx)

    # 投票交易
    vote = VoteTransaction()
    vote.valid_height = BaasManager.get_valid_height()
    vote.register_id = "25813-1"
    vote.fee_amount = 10000000
    vote.fee_coin_symbol = CoinType.WICC.value
    vote.vote_list = [
        Vote(VoteType.ADD.value, "", 200000000),
        Vote(VoteType.ADD.value, "", 200000000)
    ]
# 580190a42c0200010457494343bc834044c1cdd3cced615b17d6930a989689bb857b33519a4f75aee8d9cd5a660e9c00473045022100e2e7ce94b8536444163366e81070bc11b38597c09a137349ace4fc44c339fbad02200f053527a7eb52a00b2f5401af92499d60e3743a2d2a62932568eacee2abf1de
# 580190a42c0200010457494343bc8340009c0e665acdd9e8ae754f9a51337b85bb8996980a93d6175b61edccd3cdc144473045022100bdd57a110bc5f69452274da13ffc3bc78c9e33f98318116bc96bac6d3131c3e202206646351fd92102eb129b474f8a404e6e79d00b12d70c05c17e614f42b3d81941
# 1601c13e020001045749434383e1ac0044c1cdd3cced615b17d6930a989689bb857b33519a4f75aee8d9cd5a660e9c0096eae0000046304402205129a54de63788f0e4d47210d5b0bcb729f799173b1d04e9c6c6fcecbb6cf81502203564eae47942cc7b581dc6262ec8bffc8a81d30c33abeb9ca416568ebfcfa25f
# 1601c13e020001045749434383e1ac0044c1cdd3cced615b17d6930a989689bb857b33519a4f75aee8d9cd5a660e9c0096eae000010457494343aed6c100473045022100fb69591720aa068281905fb1fcaed62c699e52eb2f21eec25b4d5ec8672ed08602203bb5c8c4398f0cf84cf472417c9d626d736b32465f3868f01304e010d0bed5f6
# 540190a42c020001045749434383e1ac0004575553440457494343a49faec700858c20473045022100b570b4ccc8bfa77a7a169bcd5718d8c8858ac13025e8360a5d1328695952dd2f022007fdf4fbad4706514bf94a96848845cc395aa4ea983830fbbe82faee82e61967
# 540190a42c020001045749434383e1ac0004575553440457494343a49faec700858c20473045022100b570b4ccc8bfa77a7a169bcd5718d8c8858ac13025e8360a5d1328695952dd2f022007fdf4fbad4706514bf94a96848845cc395aa4ea983830fbbe82faee82e61967