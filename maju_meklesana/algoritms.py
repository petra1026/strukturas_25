import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from PIL import Image
import os
from PIL import ImageEnhance

bilzu_adrese = "maju_meklesana/bildes/"

modelis = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    min_samples_split=2,
    min_samples_leaf=1,
    random_state=42
)

def augmentacija(image):
    # Izveidojam vairākas bildes versijas
    bildes = []
    # Oriģinālā bilde
    bildes.append(np.array(image))
    
    # Spilgtuma maiņa
    enhancer = ImageEnhance.Brightness(image)
    bildes.append(np.array(enhancer.enhance(1.5)))  # Gaišāka
    bildes.append(np.array(enhancer.enhance(0.7)))  # Tumšāka
    
    # Apgriešana horizontāli
    bildes.append(np.array(image.transpose(Image.FLIP_LEFT_RIGHT)))
    
    return bildes

def modela_trenesana(modelis):
    bildes = []
    label = []

    for nosaukums in os.listdir(bilzu_adrese):
        image = Image.open(os.path.join(bilzu_adrese,nosaukums)).resize((400,400),Image.Resampling.LANCZOS)
        augmentetas_bildes = augmentacija(image)
        
        for bilde in augmentetas_bildes:
            bildes.append(bilde)
            if "maja" in nosaukums:
                label.append(1)
            else:
                label.append(0)

    bildes = np.array(bildes)
    label = np.array(label)

    bildes = bildes/255.0
    bildes = bildes.reshape(bildes.shape[0], -1)

    X_train, x_test, Y_train, y_test = train_test_split(bildes, label, test_size=0.2, random_state=42)

    modelis.fit(X_train, Y_train)

    rezultats = modelis.predict(x_test)
    precizitate = accuracy_score(rezultats, y_test)

    print(f"Modela precizitate: {precizitate:.2%}")
    return modelis

def majas_noteiksana(bilde, modelis):
    bilde = [Image.open(bilde).resize((400,400),Image.Resampling.LANCZOS)]
    bilde = np.array(bilde)
    bilde = bilde/255.0
    bilde = bilde.reshape(bilde.shape[0], -1)
    rezultats = modelis.predict(bilde)
    if rezultats[0] == 1:
        print("Saja bilde ir maja")
    else:
        print("Nav maja")
    return rezultats

# Apmacam modeli
print("Saku modela trenešanu...")
modelis = modela_trenesana(modelis)

# Parbaudam uz dažādam bildem
print("\nParbaudu dažadas bildes:")
for bilde in ["maja1.jpg", "maja2.jpg", "download1.jpg"]:
    print(f"\nParbauda bildi: {bilde}")
    majas_noteiksana(os.path.join(bilzu_adrese, bilde), modelis)
