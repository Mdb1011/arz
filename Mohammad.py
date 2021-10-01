#bitcoin

from colorma import Fore,init
init()

http = requests.get("http://get-link.ir:8000/api/v2/crypto/").text

myjson = json.load(http)

for data in myjson[`data`]


    print(Fore.GREEN+"NAME : "+Fore.WHITE+ data[`name`])
    print(Fore.GREEN+"Dollar price : "+Fore.WHITE+ data[`Dollar price`]
    print(Fore.GREEN+"Toman price : "+Fore.WHITE+ data[`Toman price`]
    print(Fore.GREEN+"Daily change : "+Fore.WHITE+ data[`Daily change`]
    print(Fore.GREEN+"weekly change : "+Fore.WHITE+ data[`weekly change`]

    print(Fore.RED+"\n####################################################")
