# Cho 1 mảng gồm các nhân vật hoạt hình:
# nhan_vat = ['Bach Tuyet”, 'Tom va Jerry”, 'Doremon”,
#             'Lo Lem”, 'Moc Lan”,  'Mickey Mouse”]

# Yêu cầu:
# Tạo mảng trống cong_chua_disney
# In ra số thứ tự của nhân vật trong mảng nhan_vat nếu nhân vật ấy là 1 công chúa Disney
# Dùng vòng lặp for với mảng nhan_vat để thêm vào mảng cong_chua_disney những nhân vật là công chúa Disney 
# In ra mảng cong_chua_disney

# Output:
# 0
# 3
# 4
# ['Bach Tuyet”, 'Lo Lem”, 'Moc Lan”]


# FILTERING EXAMPLE

# original list
nhan_vat = [
    'Bach Tuyet',
    'Tom va Jerry',
    'Doremon',
    'Lo Lem',
    'Moc Lan',
    'Mickey Mouse'
]

# filtered list, initialized as empty
cong_chua = []

# iterate over original list
for i in range(len(nhan_vat)):
    who = nhan_vat[i]

    # check if member of list is "good" or satisfies a condition
    if who in ['Bach Tuyet', 'Lo Lem', 'Moc Lan']:
        print(i)
        cong_chua.append(who)   # append "good" member to filtered list

print(cong_chua)
