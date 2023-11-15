from index import PayOS
from utils import convertObjToQueryStr, sortObjDataByKey
x =  PayOS("da5a677c-6eb4-4994-9210-7016ab67a328", "9fff2989-fa9e-4a6a-90a8-29297755c00b", "fd3e7fe088022ac96537096c96e42bb221198e69929481964b5f941fd4fd6c09")

# x.createPaymentLink({
#     "orderCode": 153423,
#     "amount": 1000,
#     "description": "Thanh toan don hang",
#     "items": [
#       {
#         "name": "Mì tôm hảo hảo ly",
#         "quantity": 1,
#         "price": 1000,
#       }
#     ],
#     "cancelUrl": "https://your-domain.com",
#     "returnUrl": "https://your-domain.com",
# })

# print(x.getPaymentLinkInfomation(53423))

# print(x.confirmWebhook("https://9c43-14-241-231-139.ngrok-free.app/payment/payos_transfer_handler"))
print(x.cancelPaymentLink(53423, "Thích nên huỷ"))
# obj = {
#     "orderCode": 53423,
#     "amount": 1000,
#     "description": "Thanh toan don hang",
#     "items": [
#       {
#         "price": 1000,
#         "name": "Mì tôm hảo hảo ly",
#         "quantity": 1,
#       }
#     ],
#     "cancelUrl": "https://your-domain.com",
#     "returnUrl": "https://your-domain.com",
# }

# sort = convertObjToQueryStr(obj)

# print(sort)