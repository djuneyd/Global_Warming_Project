from keras.models import load_model  # TensorFlow is required for Keras to work
from PIL import Image, ImageOps  # Install pillow instead of PIL
import numpy as np
import colorama
from names import shampinion, lisichka, opyata, gruzd,borowik, podberez, podocin, ruzhik, satana,suroezka,maslenok,mizena,muhomor,pautinic,poganka,lepiota,lozhlisichka,lozhopenek,galerina,zhelchi

name,score,eatable = '','',''

def Mushroom(image_path):
    global name,score,eatable
    # Disable scientific notation for clarity
    np.set_printoptions(suppress=True)

    # Load the model
    model = load_model("keras_model.h5", compile=False)

    # Load the labels
    class_names = open("labels.txt", "r", encoding="utf8").readlines()

    # Create the array of the right shape to feed into the keras model
    # The 'length' or number of images you can put into the array is
    # determined by the first position in the shape tuple, in this case 1
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    # Replace this with the path to your image
    image = Image.open(image_path).convert("RGB")

    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # turn the image into a numpy array
    image_array = np.asarray(image)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # Predicts the model
    prediction = model.predict(data)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]


    if class_name == class_names[0]:
        text = shampinion
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\sham1.jpg', 'images\sham2.jpg', 'images\sham3.jpg', 'images\sham4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=984'

    elif class_name == class_names[1]:
        text = lisichka
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\lis1.jpg', 'images\lis2.jpg', 'images\lis3.jpg', 'images\lis4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1626'

    elif class_name == class_names[2]: 
        text = opyata
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\op1.jpg', 'images\op2.jpg', 'images\op3.jpg', 'images\op4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1623'

    elif class_name == class_names[3]:
        text = gruzd
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\gr1.jpg', 'images\gr2.jpg', 'images\gr3.jpg', 'images\gr4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1625'

    elif class_name == class_names[4]:
        text = borowik
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\wel1.jpg', 'images\wel2.jpg', 'images\wel3.jpg', 'images\wel4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1010'

    elif class_name == class_names[5]:
        text = podberez
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\podber1.jpg', 'images\podber2.jpg', 'images\podber3.jpg', 'images\podber4.jpg']
        link = 'https://povar.ru/list/podberezoviki/'

    elif class_name == class_names[6]:
        text = podocin
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\podos1.jpg', 'images\podos2.jpg', 'images\podos3.jpg', 'images\podos4.jpg']
        link = 'https://povar.ru/list/podosinoviki/'

    elif class_name == class_names[7]:
        text = ruzhik
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\Rijik1.jpg', 'images\Rijik2.jpg', 'images\Rijik3.jpg', 'images\Rijik4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1624'

    elif class_name == class_names[8]:
        text = suroezka
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\siroej1.jpg', 'images\siroej2.jpg', 'images\siroej3.jpg', 'images\siroej4.jpg']
        link = 'https://www.russianfood.com/recipes/bytype/?fid=1627'

    elif class_name == class_names[9]:
        text = maslenok
        eat = 'СЪЕДОБНЫЙ'
        examples = ['images\maslen1.jpg', 'images\maslen2.jpg', 'images\maslen3.jpg', 'images\maslen4.jpg']
        link = 'https://povar.ru/list/maslyata/'

    elif class_name == class_names[10]:
        text = muhomor
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\mux1.jpg', 'images\mux2.jpg', 'images\mux3.jpg', 'images\mux4.jpg']

    elif class_name == class_names[11]:
        text = poganka
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\pogan1.jpg', 'images\pogan2.jpg', 'images\pogan3.jpg', 'images\pogan4.jpg']

    elif class_name == class_names[12]:
        text = satana
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\satana1.jpg', 'images\satana2.jpg', 'images\satana3.jpg', 'images\satana4.jpg']

    elif class_name == class_names[13]:
        text = lepiota
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\lepiota1.jpg', 'images\lepiota2.jpg', 'images\lepiota3.jpg', 'images\lepiota4.jpg']

    elif class_name == class_names[14]:
        text = galerina
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\galerina1.jpg', 'images\galerina2.jpg', 'images\galerina3.jpg', 'images\galerina4.jpg']

    elif class_name == class_names[15]:
        text = pautinic
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\pautinik1.jpg', 'images\pautinik2.jpg', 'images\pautinik3.jpg', 'images\pautinik4.jpg']

    elif class_name == class_names[16]:
        text = zhelchi
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\jelch1.jpg', 'images\jelch2.jpg', 'images\jelch3.jpg', 'images\jelch4.jpg']

    elif class_name == class_names[17]:
        text = lozhlisichka
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\lojlis1.jpg', 'images\lojlis2.jpg', 'images\lojlis3.jpg', 'images\lojlis4.jpg']

    elif class_name == class_names[18]:
        text = lozhopenek
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\lojop1.jpg', 'images\lojop2.jpg', 'images\lojop3.jpg', 'images\lojop4.jpg']

    elif class_name == class_names[19]:
        text = mizena
        eat = 'НЕ СЪЕДОБНЫЙ'
        examples = ['images\micena1.jpg', 'images\micena2.jpg', 'images\micena3.jpg', 'images\micena4.jpg']


    if eat == 'СЪЕДОБНЫЙ':
        lst = [eat, class_name[2:], confidence_score, text, examples, link]
    else:
        lst = [eat, class_name[2:], confidence_score, text, examples]
    return lst