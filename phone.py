#creating info card for phone
phone_brand = "Realme 14 pro"
phone_model = "RMX3612"
storage_capacity = 256
ram_inbuilt = 12
battery_capacity = 5000
price = 35000
is_5g_supported =True
support_5g = "Yes 5G supported" if is_5g_supported else "No, 5G not supported"
is_available =True
availability_status = "Available in market" if is_available else "Not available in market"

print("======= PHONE INFO CARD =======")

print(f"PHONE BRAND:{phone_brand}")
print(f"PHONE MODEL:{phone_model}")
print(f"STORAGE CAPACITY:{storage_capacity}GB")
print(f"RAM:{ram_inbuilt}GB")
print(f"BATTERY CAPACITY:{battery_capacity}mAh")
print(f"PRICE:{price}")
print(f"5G SUPPORT:{support_5g}")
print(f"AVAILABILITY:{availability_status}")

print("================================")