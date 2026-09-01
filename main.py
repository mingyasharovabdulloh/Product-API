import json
import requests

url=requests.get("https://dummyjson.com/products").json()



products=url['products']
# with open('1_chisi.json', mode='w', encoding='utf-8') as birinchisi:
#     json.dump(products, birinchisi , indent=4 , ensure_ascii=False)

# for product in products:
#     if product['id'] == 2:
#         print(product)


# for product in products:
#     if product['id'] ==1:
#         print(f"Title : {product['title']} \nPrice : {product['price']}\nCategory : {product['category']}")


# for product in products:
#     print(f"Product title : {product["title"]}")

# for product in products:
#     print(f"Product prices : {product['price']}")

# for product in products:
#     print(f"{product['id']} - {product['title']} - ${product['price']}")

# for product in products:
#     if int(product['price']) > 50:
#         print(f"{product['title']} - $ {product['price']}")

# for product in products:
#     if product['category'].lower() == "beauty":
#         print(product)

# for product in products:
#     if int(product['stock']) < 10:
#         print(product)

# for product in products:
#     if float(product['rating']) > 4:
#         print(product)

# for product in products:
#     if product['brand'] == 'Essence':
#         print(product)

# total=0
# for product in products:
#     total+=float(product['price'])
# print(f"Total : ${total}")

# summa=0
# soni=0
# for product in products:
#     soni+=int(product['stock'])
#     summa+=float(product['price'])*int(product['stock'])

# ortacha=summa/soni
# print(f"Mahsulotlarning o'rtacha qiymati : $ {ortacha}")

# max=0
# for product in products:
#     if float(product['price']) > max:
#         max=float(product['price'])
#         nomi=product['title']
# print(f"Eng qimmat product\n"
#       f"Nomi : {nomi}\n"
#       f"Narxi : {max}")
    
# min=5
# for product in products:
#     if float(product['price']) < min:
#         min=float(product['price'])
#         nomi=product['title']
# print(f"Eng qimmat product\n"
#       f"Nomi : {nomi}\n"
#       f"Narxi : {min}")

# max_stock=0
# for product in products:
#     if int(product['stock']) > max_stock:
#         max_stock=int(product['stock'])
#         title_product=product['title']
# print("Eng katta stock ga eka product\n"
#       f"Title : {title_product}\n"
#       f"Max stock : {max_stock}")

# max_rating=0
# for product in products:
#     if float(product['rating']) > max_rating:
#         max_rating=float(product['rating'])
#         title=product['title']
#
# print("Eng katta rating ga ega product\n"
#       f"Title : {title}\n"
#       f"Rating : {max_rating}")

# names=[]
# for product in products:
#     names.append(product['title'])
#
# print(names)

# expensive_product=[]
# for product in products:
#     if float(product['price']) > 50 :
#         expensive_product.append(product['title'])

# print(expensive_product)

# new_list=[]
# for product in products:
#     if product['category'] == 'beauty':
#         new_list.append(product)

# print(new_list)

# new_list=[]
# for product in products:
#     if float(product['rating']) > 4:
#         new_list.append({
#             'title' : product['title'],
#             'rating' : float(product['rating'])
#         })
        
# print(new_list)

# for product in products:
#     print(float(product['dimensions']['width']))
#     break;

# list=[]
# for product in products:
#     list.append({
#         'title' : product['title'],
#         'width' : product['dimensions']['width'],
#         'height' : product['dimensions']['height'],
#         'depth' : product['dimensions']['depth']
#     })

# print(list)

# for product in products:
#     if float(product['dimensions']['width']) > 20:
#         print(product)

# for product in products:
#     print(product['tags'])

# list=[]
# for product in products:
#     list.append({
#         'id' : int(product['id']),
#         'tags' : product['tags']
#     })

# print(list)

# for product in products:
#     for tag in product['tags']:
#         if tag == 'perfumes':
#             print(product)

# for product in products:
#     for names in product['reviews']:
#         print(f"{names['reviewerName']}")
#     break;

# for product in products:
#     print(f"Title : {product['title']}\n"
#           f"Names of reviewes :")
#     for names in product['reviews']:
#         print(f"{names['reviewerName']}")
#     print("\n")

# for product in products:
#     print(f"Product : {product['title']}")
#     for names in product['reviews']:
#         if float(names['rating']) == 5:
#             print(f"Reviewer : {names['reviewerName']}"
#                   f"Comment : {names['comment']}")

#     print('\n')

# with open('products.json', mode='w', encoding='utf-8') as file:
#     json.dump( url, file, indent=4 , ensure_ascii= False)

# json_data=[]
# for product in products:
#     json_data.append({
#         'title' : product['title'],
#         'price' : product['price'],
#         'category' : product['category']
#     })
# with open('selected_products.json', mode='w', encoding='utf-8') as file:
#     json.dump(json_data, file, indent=4, ensure_ascii=False)

# url=requests.get("https://dummyjson.com/products?limit=5").json()
# print(url)

# url=requests.get("https://dummyjson.com/products?limit=5&skip=5").json()
# print(url)

# url=requests.get("https://dummyjson.com/products?limit=10").json()
# print(url)

# url=requests.get("https://dummyjson.com/products?limit=10&skip=10").json()
# print(url)


# LOYIHA

print("--------------- Online dokonimizga xush kelibsiz -------------------") 

while True:

    print("=====================================================================")
    print("---------- Raqamni yozish orqali operatsiyani tanglang --------------\n")

    print(f"                 1. Barcha productlar\n"
        f"                 2. Qimmat productlar\n"
        f"                 3. Arzon productlar\n"
        f"                 4. Beauty productlar\n"
        f"                 5. Eng qimmat product\n"
        f"                 6. Eng arzon product\n"
        f"                 7. Rating bo'yicha\n"
        f"                 8. Product qidirish\n"
        f"                 9. JSON faylga saqlash\n"
        f"                 0. Exit"
        )


    print("======================================================================")
    print("Eslatib o'tamiz 0 raqamini tanlamagunizcha dastur tugatilmaydi !\n")
    
    option=input("Operatsiya raqamini kiriting --> ")
    print(" ")

    if option == "0":
    
        print("Dastur toxtatildi !")
        break;

    elif option == "1":

        for product in products:
            print(f"Name of prodct : {product['title']}\n"
                f"Price : $ {product['price']}\n"
                f"Rating : {float(product['rating'])}\n"
                f"Stock : {int(product['stock'])}"
                )
            print('------------------------------------------\n')

    elif option == "2":

        for product in products:
            if int(product['price'])>100:
                print(f"Name of prodct : {product['title']}\n"
                    f"Price : $ {product['price']}\n"
                    f"Rating : {float(product['rating'])}\n"
                    f"Stock : {int(product['stock'])}"
                    )
                print('------------------------------------------\n')

            
    elif option == "3":
        for product in products:
            if int(product['price'])<100:
                print(f"Name of prodct : {product['title']}\n"
                    f"Price : $ {product['price']}\n"
                    f"Rating : {float(product['rating'])}\n"
                    f"Stock : {int(product['stock'])}"
                    )
                print('------------------------------------------\n')

    elif option == "4":

        for product in products:
            if product['category'] == "beauty":
                print(f"Name of prodct : {product['title']}\n"
                    f"Price : $ {product['price']}\n"
                    f"Rating : {float(product['rating'])}\n"
                    f"Stock : {int(product['stock'])}"
                    )
                print('------------------------------------------\n')

    elif option == "5":

        list=[]
        max=0

        for product in products:

            if int(product['price']) > max:
                max=int(product['price'])
                list.clear()
                list.append(product)

        for product in list:
            print(f"Name of prodct : {product['title']}\n"
                f"Price : $ {product['price']}\n"
                f"Rating : {float(product['rating'])}\n"
                f"Stock : {int(product['stock'])}"
                )
            
    elif option == "6":

        list=[]
        min=5

        for product in products:
            if int(product['price']) < min:
                min=int(product['price'])
                list.clear()
                list.append(product)

        for product in list:
            print(f"Name of prodct : {product['title']}\n"
                f"Price : $ {product['price']}\n"
                f"Rating : {float(product['rating'])}\n"
                f"Stock : {int(product['stock'])}"
                )
            
    elif option == "7":

        products=url["products"]
        products=sorted(products, key=lambda product : product['rating'], reverse=True)
        for product in products:
           print(f"Name of prodct : {product['title']}\n"
                 f"Price : $ {product['price']}\n"
                 f"Rating : {float(product['rating'])}\n"
                 f"Stock : {int(product['stock'])}"
                )
           print('------------------------------------------\n')

    elif option == "8":

        name_of_product=input("Mahsulot nomini kiriting --> ")
        print('\n')
        found=False

        for product in products:
            for tag in product['tags']:
                if tag == name_of_product.lower():
                    print(f"Name of prodct : {product['title']}\n"
                        f"Price : $ {product['price']}\n"
                        f"Rating : {float(product['rating'])}\n"
                        f"Stock : {int(product['stock'])}"
                        )
                    print('------------------------------------------\n')

                    found=True
                    break;
        
        if not found:
            print("Bunday mahsulot mavjud emas !")
            print(' ')

    elif option == "9":
    
        name_of_product=input("Korzinka ga olib qo'yish uchun mahsulot nomini kiritng --> ")
        print(' ')
        data=[]
        found=False

        for product in products:
            for tag in product['tags']:
                if tag == name_of_product.lower():
                    data.append({
                        'Name of product' : product['title'],
                        'Price' : product['price'],
                        'Rating' : product['rating'],
                        'Stock' : product['stock']
                    })

                    with open("korzinka.json", mode='w', encoding='utf-8') as file:
                        json.dump(data, file ,indent=4 ,ensure_ascii=False)

                    print("Mahsulot korzinkaga qo'shildi")
                    print(' ')
                    found=True

        if not found:
            print("Bunday mahsulot mavjud emas !")
            print(" ")

    else:
        print("Siz xato raqamni kiritdingiz !")

    
