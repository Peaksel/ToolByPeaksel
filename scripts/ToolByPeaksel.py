# A helper script for AUTOMATIC1111/stable-diffusion-webui.

import copy
import os
import random
from os import listdir, path
from os.path import isfile, join

import modules.scripts as scripts
import gradio as gr
from modules.processing import Processed, process_images
from modules.shared import cmd_opts, opts, state
from modules import scripts

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
# directories

MediumsDir = os.path.join(scripts.basedir(), f"Mediums/")
MediumsSubDir = os.path.join(scripts.basedir(), f"Mediums/SubMediums/")
BeautifiersDir = os.path.join(scripts.basedir(), f"Beautifiers/")
ColorsDir = os.path.join(scripts.basedir(), f"Colors/")
CameraSettingsDir = os.path.join(scripts.basedir(), f"CameraSettings/")
ArtistDir = os.path.join(scripts.basedir(), f"Artists/")
def FilesInFolder(SourceFolder):
    return [file for file in os.listdir(SourceFolder)]

def FilesInFolderFullPath(SourceFolder):
    return [SourceFolder + file for file in os.listdir(SourceFolder)]
def random_all_camera(x):
    return "Random"

def random_all_favs_camera(x):
    return "Random From Favs"
def reset_all_camera(x):
    return "Not set"
def reset_all_camera_value(x):
    return 1.3
#"3D Rendering": ",Highly detailed,Art by senior Artist,Polycount,trending on CGSociety,trending on ArtStation",
#"Photo": ",HD,4K,8K,highly detailed,Sharp,Photo-realism,Professional photograph,Masterpiece",
    

#my methods

def PrintPrompt(prompt, strength, text):
    FinalPrompt = ""
    if prompt != "Not set":
        if prompt == "Random":  
            FinalPrompt = " (" + random.choice(
                ListFromDropDown(prompt)) + ":" + str(strength) + ") "
        else:
            FinalPrompt = " (" + prompt.value.replace("*","") + \
                ":" + str(strength) + ") "
    else:
        FinalPrompt = ""
    print(FinalPrompt)
    text = FinalPrompt

#konvertuj dropdown u listu bez random
def ListFromDropDown(drop):
    newList = []
    defList = drop.choices
    for line in defList:
        line = line.replace("*","")
        if(((line != "Not set") and (line != "Random")) and (line != "Random From Favs")):
            newList.append(line)
    return newList

#artists
def Dropdown_List_From_ArtistFile(x,y,addDefaults):
    PromptValues = []
    file1 = open(ArtistDir + x + '.txt', encoding = 'utf-8',mode = 'r')
    Lines = file1.readlines()
    hasFavs = False
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])

        count += 1
    PromptValues = sorted(PromptValues)
    if(hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults):
        PromptValues = ["Not set", "Random"] + PromptValues

    return gr.Dropdown(PromptValues, label=y, value="Not set")

def RandomFromArtist(x):
    randomList = []
    file1 = open(ArtistDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList
def RandomFavFromArtists(x):
    randomList = []
    file1 = open(ArtistDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList
#camera settings
def Dropdown_List_From_CamerasFile(x,y,addDefaults):
    PromptValues = []
    hasFavs = False
    file1 = open(CameraSettingsDir + x + '.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])

        count += 1
    PromptValues = sorted(PromptValues)
    if (hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults):
        PromptValues = ["Not set", "Random"] + PromptValues

    return gr.Dropdown(PromptValues, label=y, value="Not set")

def RandomFromCameras(x):
    randomList = []
    file1 = open(CameraSettingsDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList
def RandomFavFromCameras(x):
    randomList = []
    file1 = open(CameraSettingsDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList
#colors ColorSchemes ColorTones
def Dropdown_List_From_ColorsFile(x,y,addDefaults):
    PromptValues = []
    file1 = open(ColorsDir + x + '.txt', 'r')
    Lines = file1.readlines()
    hasFavs = False
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])

        count += 1
    PromptValues = sorted(PromptValues)
    if (hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults):
        PromptValues = ["Not set", "Random"] + PromptValues

    return gr.Dropdown(PromptValues, label=y, value="Not set")

def RandomFromColors(x):
    randomList = []
    file1 = open(ColorsDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList
def RandomFavFromColors(x):
    randomList = []
    file1 = open(ColorsDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList
#cita listu beautifiera   
def Dropdown_List_From_BeautifierFile(x,y,addDefaults):
    PromptValues = []
    file1 = open(BeautifiersDir+x+'.txt', 'r')
    Lines = file1.readlines()
    hasFavs = False
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])
       
        count += 1
    PromptValues = sorted(PromptValues)
    if (hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults):
        PromptValues = ["Not set", "Random"] + PromptValues
   
    return gr.Dropdown(PromptValues, label=y, value="Not set")


def RandomBeautifier(x):
    randomList = []
    file1 = open(BeautifiersDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList

def RandomFavBeautifier(x):
    randomList = []
    file1 = open(BeautifiersDir + x + '.txt', 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList


#cita listu mediuma
def RandomMedium(x):
    randomList = []
    file1 = open(MediumsDir + x + '.txt', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList

def RandomFavMedium(x):
    randomList = []
    file1 = open(MediumsDir + x + '.txt', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList
def Dropdown_List_From_MediumFile(x,y,addDefaults):
    PromptValues = []
    file1 = open(MediumsDir+x+'.txt', 'r')
    Lines = file1.readlines()
    hasFavs = False
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])
        count += 1
    PromptValues = sorted(PromptValues)
    if (hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults):
        PromptValues = ["Not set", "Random"] + PromptValues
    
    return gr.Dropdown(PromptValues, label=y, value="Not set")
#cita listu pod-mediuma     

def RandomSubMedium(x):
    randomList = []
    file1 = open(MediumsSubDir+str(x).replace("*","")+'.txt', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        randomList.append(xNew[0])

    return randomList


def RandomFavSubMedium(x):
    randomList = []
    file1 = open(MediumsSubDir + str(x).replace("*", "") + '.txt', 'r')
    Lines = file1.readlines()

    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (xNew[4] == "True"):
            randomList.append(xNew[0])

    return randomList
def Dropdown_List_From_SubMediumFile(x,y,addDefaults):
    PromptValues = []
    file1 = open(MediumsSubDir+str(x).replace("*","")+'.txt', 'r')
    Lines = file1.readlines()
    hasFavs = False
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])
      
        count += 1
    PromptValues = sorted(PromptValues)
    if (hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues
    if (addDefaults and count>1):
        PromptValues = ["Random"] + PromptValues
        PromptValues = ["Disabled"] + PromptValues;
    
    return gr.Dropdown(PromptValues, label=y, value=PromptValues[0])
#refreshuje listu pod-mediuma   
def RefreshDropDown(name):
    PromptValues = []
    hasFavs = False
    file1 = open(MediumsSubDir+str(name).replace("*","")+'.txt', 'r')
    Lines = file1.readlines()
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[4] == "True"):
            hasFavs = True
            PromptValues.append("*" + xNew[0])
        else:
            PromptValues.append(xNew[0])
        count += 1
    PromptValues = sorted(PromptValues)
    
    if(hasFavs):
        PromptValues = ["Random From Favs"] + PromptValues;
    if(count>1):
        PromptValues = ["Disabled", "Random"] + PromptValues;
    return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0])



def GetPositivesFromMedium(mediumName):
    file1 = open(MediumsDir+"MediumType"+'.txt', 'r')
    Lines = file1.readlines()
    positives = ""
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[0] == str(mediumName).replace("*","")):
            positives = xNew[2]

    return positives  

    
def GetPositivesFromSubMedium(mediumName, subMediumName):
    file1 = open(MediumsSubDir+str(mediumName).replace("*","")+'.txt', 'r')
    Lines = file1.readlines()
    positives = ""
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[0] == str(subMediumName).replace("*","")):
            positives = xNew[2]

    return positives 
    
def GetNegativesFromMedium(mediumName):
    file1 = open(MediumsDir+"MediumType"+'.txt', 'r')
    Lines = file1.readlines()
    negatives = ""
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[0] == str(mediumName).replace("*","")):
            negatives = xNew[3]

    return negatives  

    
def GetNegativesFromSubMedium(mediumName, subMediumName):
    file1 = open(MediumsSubDir+str(mediumName).replace("*","")+'.txt', 'r')
    Lines = file1.readlines()
    negatives = ""
    count = 0
    # Strips the newline character
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if(xNew[0] == str(subMediumName).replace("*","")):
            negatives = xNew[3]

    return negatives 
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

AlwaysBad = ""
promptButtonText = ""
class Script(scripts.Script):
    txt2img_prompt = None
    img2img_prompt = None
    batch_count = None
    batch_size = None
    steps = None
    

    def after_component(self, component, **kwargs):
        if kwargs.get('elem_id') == 'txt2img_prompt':
            self.txt2img_prompt = component
        if kwargs.get('elem_id') == 'img2img_prompt':
            self.img2img_prompt = component
        # if kwargs.get('elem_id') == 'batch_count':
        #     self.batch_count = component
        # if kwargs.get('elem_id') == 'batch_size':
        #     self.batch_size = component
        # if kwargs.get('elem_id') == 'steps':
        #     self.steps = component

    def title(self):
        return "Tool by Peaksel"

    def show(self, is_img2img):
        return True


    def ui(self, is_img2img):
        gr.HTML('<br />')
        with gr.Tab("Parameters"):
            
            with gr.Row(variant = "panel"):
                #Beautifiers
                ddResultConcept = Dropdown_List_From_BeautifierFile("Beautifiers", "Beautifiers", True)
                gr.Label(value = "", label = "", visible = "False", interactive = "False", show_label = "False").style(container = False)
                slBeautifierStrength = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
            with gr.Column(variant = "panel"):
                with gr.Row():
                    #Mediums
                    ddMediumType = Dropdown_List_From_MediumFile("MediumType","Medium Type", True)
                    ddMediumSubType = Dropdown_List_From_SubMediumFile(ddMediumType,"Medium sub-type", True)
                    ddMediumType.change(RefreshDropDown, ddMediumType, ddMediumSubType)
                    slMediumStrength = gr.Slider(
                        0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Row():
                    cbMediumPositives = gr.Checkbox(value = True, label = "Enable Positives")
                    cbMediumNegatives = gr.Checkbox(value = True, label = "Enable Negatives")
            with gr.Row(variant = "panel"):
                #Colors
                ddColorTone = Dropdown_List_From_ColorsFile("ColorTones", "Colors Tone", True)
                ddColorScheme = Dropdown_List_From_ColorsFile("ColorSchemes", "Color Schemes", True)
                slResultColorStrength = gr.Slider(
                    0, 2, value=1.0, step=0.05, show_label=False)

          
            with gr.Column(variant="panel"):
                with gr.Row():
                    strSequentialPrompt = gr.Textbox(
                        lines=3, label="Sequential prompts [X]", placeholder="Insert [X] anywhere in main prompt to sequentially insert values from here. Random values will be added here or to main prompt.")
                with gr.Row():
                    strSubSequentialPrompt = gr.Textbox(
                        lines=3, label="SubSequential prompts [Y]", placeholder="Insert [Y] in the final prompt <== to sequentially insert values from here (and increase prompt count). This is done after all other prompts and loops through all lines.")

                with gr.Row():
                    strRandomPromptA = gr.Textbox(
                        lines=3, label="Random [A]", placeholder="Insert [A] anywhere in main prompt (or [X] prompt) to randomly insert values from here.")
                    strRandomPromptB = gr.Textbox(
                        lines=3, label="Random [B]", placeholder="Insert [B] anywhere in main prompt (or [X] prompt) to randomly insert values from here.")
                    strRandomPromptC = gr.Textbox(
                        lines=3, label="Random [C]", placeholder="Insert [C] anywhere in main prompt (or [X] prompt) to randomly insert values from here.")


            #Camera stuff
            with gr.Column(variant="panel"):
                with gr.Column(variant="panel"):
                    with gr.Row():
                        randomCameraButton = gr.Button('Random From All')
                        randomFavsCameraButton = gr.Button('Random From Favs')
                        resetCameraButton = gr.Button('Reset All', variant = 'stop')
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddResultCameraShotType = Dropdown_List_From_CamerasFile("CameraShotType", "Camera Shot Type", True)
                        ddResultCameraShotAngle = Dropdown_List_From_CamerasFile("CameraShotAngle", "Camera Shot Angle", True)
                        slCameraGroup1 = gr.Slider(0, 2, value=1.3, step=0.05, label="Influence")
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddResultCameraBrand = Dropdown_List_From_CamerasFile("CameraBrand", "Camera Brand", True)
                        ddResultCameraFilmSize = Dropdown_List_From_CamerasFile("CameraFilmSize", "Camera Film Size", True)
                        slCameraGroup2 = gr.Slider(0, 2, value=1.0, step=0.05, label="Influence")
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddResultCameraFocus = Dropdown_List_From_CamerasFile("CameraFocus", "Camera Focus", True)
                        ddResultCameraFocalLength = Dropdown_List_From_CamerasFile("CameraFocalLength", "Camera Focal Length", True)
                        slCameraGroup3 = gr.Slider(0, 2, value=1.3, step=0.05, label="Influence")

                randomCameraButton.click(random_all_camera,inputs=ddResultCameraShotType, outputs=ddResultCameraShotType)
                randomCameraButton.click(random_all_camera,inputs=ddResultCameraShotAngle, outputs=ddResultCameraShotAngle)
                randomCameraButton.click(random_all_camera,inputs=ddResultCameraBrand, outputs=ddResultCameraBrand)
                randomCameraButton.click(random_all_camera,inputs=ddResultCameraFilmSize, outputs=ddResultCameraFilmSize)
                randomCameraButton.click(random_all_camera,inputs=ddResultCameraFocus, outputs=ddResultCameraFocus)
                randomCameraButton.click(random_all_camera,inputs=ddResultCameraFocalLength, outputs=ddResultCameraFocalLength)

                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraShotType, outputs=ddResultCameraShotType)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraShotAngle, outputs=ddResultCameraShotAngle)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraBrand, outputs=ddResultCameraBrand)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraFilmSize, outputs=ddResultCameraFilmSize)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraFocus, outputs=ddResultCameraFocus)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddResultCameraFocalLength, outputs=ddResultCameraFocalLength)
                   
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraShotType, outputs=ddResultCameraShotType)
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraShotAngle, outputs=ddResultCameraShotAngle)
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraBrand, outputs=ddResultCameraBrand)
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraFilmSize, outputs=ddResultCameraFilmSize)
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraFocus, outputs=ddResultCameraFocus)
                resetCameraButton.click(reset_all_camera,inputs=ddResultCameraFocalLength, outputs=ddResultCameraFocalLength)


                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup1, outputs=slCameraGroup1)
                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup2, outputs=slCameraGroup2)
                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup3, outputs=slCameraGroup3)
                
                
            with gr.Column(variant="panel"):
                with gr.Row():
                    ddArtistSingle = Dropdown_List_From_ArtistFile("Artists", "Artist", True)
                    ddArtistSimilar = Dropdown_List_From_ArtistFile("ArtistTheme", "Artist Theme", True)
                    slArtistGroupStrength = gr.Slider(0, 2, value=1.5, step=0.05, label="Influence")
                
            with gr.Column(variant="panel"):
                with gr.Row():
                    cbChangeCount = gr.Checkbox(
                        value=True, label="Set batch count to prompt count")
                    cbIncreaseSeed = gr.Checkbox(
                        value=False, label="Increase seed with batch size")
        with gr.Tab("Character"):
            with gr.Column(variant="panel"):
                gr.Label("To be continued")
            
            
        return [ddResultConcept,
                cbChangeCount,
                cbIncreaseSeed,
                strSequentialPrompt,
                strSubSequentialPrompt,
                strRandomPromptA,
                strRandomPromptB,
                strRandomPromptC,
                slMediumStrength,
                ddMediumType,
                ddColorTone,
                ddColorScheme,
                slResultColorStrength,
                slBeautifierStrength,
                ddResultCameraShotType,
                ddResultCameraShotAngle,
                ddResultCameraBrand,
                ddResultCameraFilmSize,
                ddResultCameraFocus,
                ddResultCameraFocalLength,
                slCameraGroup1,
                slCameraGroup2,
                slCameraGroup3,
                ddArtistSingle,
                ddArtistSimilar,
                slArtistGroupStrength,
                cbMediumPositives,
                cbMediumNegatives,
                ddMediumSubType
                ]

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

    def run(self, p,
            ddResultConcept,
            cbChangeCount,
            cbIncreaseSeed,
            strSequentialPrompt: str,
            strSubSequentialPrompt: str,
            strRandomPromptA: str,
            strRandomPromptB: str,
            strRandomPromptC: str,
            slMediumStrength,
            ddMediumType,
            ddColorTone,
            ddColorScheme,
            slResultColorStrength,
            slBeautifierStrength,
            ddResultCameraShotType,
            ddResultCameraShotAngle,
            ddResultCameraBrand,
            ddResultCameraFilmSize,
            ddResultCameraFocus,
            ddResultCameraFocalLength,
            slCameraGroup1,
            slCameraGroup2,
            slCameraGroup3,
            ddArtistSingle,
            ddArtistSimilar,
            slArtistGroupStrength,
            cbMediumPositives,
            cbMediumNegatives,
            ddMediumSubType
            ):

        # If it's all empty just exit function.
        if len(p.prompt) == 0:
            print(
                f"\nEmpty prompt! It helps to have at least some guidance for SD. Remember to insert an [X], [A] or [B] into main prompt if you want to use variable values.")
            return

        # Batch lines present?
        BatchLines = [x.strip() for x in strSequentialPrompt.splitlines()]
        LineCount = len(BatchLines)

        SubBatchLines = [x.strip() for x in strSubSequentialPrompt.splitlines()]
        SubLineCount = len(SubBatchLines)

        TempText = ""
        SubTempText = ""

        images = []
        seeds = []
        prompts = []
        infotexts = []

        # Overtake amounts of things to generate so we can go through different variables
        MainJobCount = p.n_iter
        p.n_iter = 1

        SubIterationCount = p.batch_size
        p.batch_size = 1

        # If we have [X] variables use their amount, unless unchecked
        if cbChangeCount == True and len(strSequentialPrompt) > 0:
            MainJobCount = LineCount

        SubCycleCount = 1

        if SubLineCount > 0:
            SubCycleCount = SubLineCount

        # Any random lines present?
        RandomLinesA = [r.strip() for r in strRandomPromptA.splitlines()]
        RandomLinesB = [r.strip() for r in strRandomPromptB.splitlines()]
        RandomLinesC = [r.strip() for r in strRandomPromptC.splitlines()]

        # So the progress bar works correctly
        state.job_count = MainJobCount * SubIterationCount * SubCycleCount

        CurrentChoice = 0
        SubCurrentChoice = 0

        FinalResultDirection = ""

        for x in range(MainJobCount):
            SeedStep = 0

            AllMovements = ""
            AllArtists = ""

            # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

            # Large artist selection
           

            # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

            

            # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

            for y in range(SubIterationCount):

                # Clear the variables so random selection can work
                FinalResultMood = ""
                FinalResultColor = ""
                FinalConcept = ""

                # Preset the selection variables
                MainType = ""

                TypeFront = ""
                TypePositives = ""
                TypeNegatives = ""


                CameraResult1 = ""
                CameraResult2 = ""
                CameraResult3 = ""

                ArtistResult = ""
                

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                #beautifier
                if ddResultConcept != "Not set":
                    if ddResultConcept == "Random":  
                        FinalConcept = " (" + random.choice(
                            RandomBeautifier("Beautifiers")) + ":" + str(slBeautifierStrength) + ") "
                    elif ddResultConcept == "Random From Favs":
                        FinalConcept = " (" + random.choice(
                            RandomFavBeautifier("Beautifiers")) + ":" + str(slBeautifierStrength) + ") "
                    else:
                        FinalConcept = " (" + ddResultConcept.replace("*","") + \
                            ":" + str(slBeautifierStrength) + ") "
                else:
                    FinalConcept = ""
                print("final: "+FinalConcept)
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                #medium

                if(ddMediumSubType == "Disabled"):
                    if ddMediumType != "" and ddMediumType!= "Not set":
                        # If it is random, give it a random value
                        if ddMediumType == "Random":
                            MediumRandom = random.choice(RandomMedium("MediumType"))
                            MainType = " (" + MediumRandom.replace("*","") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromMedium(MediumRandom)
                            TypeNegatives = GetNegativesFromMedium(MediumRandom)
                        elif ddMediumType == "Random From Favs":
                            MediumRandom = random.choice(RandomFavMedium("MediumType"))
                            MainType = " (" + MediumRandom.replace("*","") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromMedium(MediumRandom)
                            TypeNegatives = GetNegativesFromMedium(MediumRandom)
                        # otherwise use the selected value
                        else:
                            MainType = " (" + ddMediumType.replace("*","") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromMedium(ddMediumType)
                            TypeNegatives = GetNegativesFromMedium(ddMediumType)
                else:
                    if ddMediumSubType != "" and ddMediumSubType!= "Not set":
                        if ddMediumSubType == "Random":
                            SubMediumRandom = random.choice(RandomSubMedium(ddMediumType))
                            MainType = " (" + SubMediumRandom.replace("*","") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromSubMedium(ddMediumType, SubMediumRandom)
                            TypeNegatives = GetNegativesFromSubMedium(ddMediumType, SubMediumRandom)
                        elif ddMediumSubType == "Random From Favs":
                            SubMediumRandom = random.choice(RandomFavSubMedium(ddMediumType))
                            MainType = " (" + SubMediumRandom.replace("*", "") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromSubMedium(ddMediumType, SubMediumRandom)
                            TypeNegatives = GetNegativesFromSubMedium(ddMediumType, SubMediumRandom)
                        # otherwise use the selected value
                        else:
                            MainType = " (" + ddMediumSubType.replace("*","") + ":" + str(slMediumStrength) + ") "
                            TypePositives = GetPositivesFromSubMedium(ddMediumType, ddMediumSubType)
                            TypeNegatives = GetNegativesFromSubMedium(ddMediumType, ddMediumSubType)
                
                
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                #Camera stuff
                #ddResultCameraShotType,
                #ddResultCameraShotAngle,

                #ddResultCameraBrand,
                #ddResultCameraFilmSize,

                #ddResultCameraFocus,
                #ddResultCameraFocalLength,

                #slCameraGroup1,
                #slCameraGroup2,
                #slCameraGroup3,

                #CameraResult1 = ""
                #CameraResult2 = ""
                #CameraResult3 = ""


                #section1
                if ddResultCameraShotAngle == "Not set" and ddResultCameraShotType == "Not set":
                    CameraResult1 = ""
                elif ddResultCameraShotAngle!="Not set" and ddResultCameraShotType!="Not set":
                    ShotType = ""
                    ShotAngle = ""
                    if ddResultCameraShotType == "Random":
                        ShotType = random.choice(RandomFromCameras("CameraShotType"))
                    elif ddResultCameraShotType == "Random From Favs":
                        ShotType = random.choice(RandomFavFromCameras("CameraShotType"))
                    else:
                        ShotType = ddResultCameraShotType.replace("*", "")
                    if ddResultCameraShotAngle == "Random":
                        ShotAngle = random.choice(RandomFromCameras("CameraShotAngle"))
                    elif ddResultCameraShotAngle == "Random From Favs":
                        ShotAngle = random.choice(RandomFavFromCameras("CameraShotAngle"))
                    else:
                        ShotAngle = ddResultCameraShotAngle.replace("*", "")
                    CameraResult1 = ", (" + ShotType + ", " + ShotAngle + ":" + str(slCameraGroup1) + ") "

                elif ddResultCameraShotAngle == "Not set":
                    if ddResultCameraShotType == "Random":
                        CameraResult1 = ", (" + random.choice(
                            RandomFromCameras("CameraShotType")) + ":" + str(slCameraGroup1) + ") "
                    elif ddResultCameraShotType == "Random From Favs":
                        CameraResult1 = ", (" + random.choice(
                            RandomFavFromCameras("CameraShotType")) + ":" + str(slCameraGroup1) + ") "
                    else:
                        CameraResult1 = ", (" + ddResultCameraShotType.replace("*","") + \
                            ":" + str(slCameraGroup1) + ") "
                elif ddResultCameraShotType == "Not set":
                    if ddResultCameraShotAngle == "Random":
                        CameraResult1 = ", (" + random.choice(
                            RandomFromCameras("CameraShotAngle")) + ":" + str(slCameraGroup1) + ") "
                    elif ddResultCameraShotAngle == "Random From Favs":
                        CameraResult1 = ", (" + random.choice(
                            RandomFavFromCameras("CameraShotAngle")) + ":" + str(slCameraGroup1) + ") "
                    else:
                        CameraResult1 = ", (" + ddResultCameraShotAngle.replace("*","") + \
                            ":" + str(slCameraGroup1) + ") "
                # section2
                if ddResultCameraFilmSize == "Not set" and ddResultCameraBrand == "Not set":
                    CameraResult2 = ""
                elif ddResultCameraFilmSize != "Not set" and ddResultCameraBrand != "Not set":
                    ShotBrand = ""
                    ShotSize = ""
                    if ddResultCameraBrand == "Random":
                        ShotBrand = random.choice(RandomFromCameras("CameraBrand"))
                    elif ddResultCameraBrand == "Random From Favs":
                        ShotBrand = random.choice(RandomFavFromCameras("CameraBrand"))
                    else:
                        ShotBrand = ddResultCameraBrand.replace("*", "")
                    if ddResultCameraFilmSize == "Random":
                        ShotSize = random.choice(RandomFromCameras("CameraFilmSize"))
                    elif ddResultCameraFilmSize == "Random From Favs":
                        ShotSize = random.choice(RandomFavFromCameras("CameraFilmSize"))
                    else:
                        ShotSize = ddResultCameraFilmSize.replace("*", "")
                    CameraResult2 = ", (" + ShotBrand + ", " + ShotSize + ":" + str(slCameraGroup2) + ") "

                elif ddResultCameraFilmSize == "Not set":
                    if ddResultCameraBrand == "Random":
                        CameraResult2 = ", (" + random.choice(
                            RandomFromCameras("CameraBrand")) + ":" + str(slCameraGroup2) + ") "
                    elif ddResultCameraBrand == "Random From Favs":
                        CameraResult2 = ", (" + random.choice(
                            RandomFavFromCameras("CameraBrand")) + ":" + str(slCameraGroup2) + ") "
                    else:
                        CameraResult2 = ", (" + ddResultCameraBrand.replace("*", "") + \
                                        ":" + str(slCameraGroup2) + ") "
                elif ddResultCameraBrand == "Not set":
                    if ddResultCameraFilmSize == "Random":
                        CameraResult2 = ", (" + random.choice(
                            RandomFromCameras("CameraFilmSize")) + ":" + str(slCameraGroup2) + ") "
                    elif ddResultCameraFilmSize == "Random From Favs":
                        CameraResult2 = ", (" + random.choice(
                            RandomFavFromCameras("CameraFilmSize")) + ":" + str(slCameraGroup2) + ") "
                    else:
                        CameraResult2 = ", (" + ddResultCameraFilmSize.replace("*", "") + \
                                        ":" + str(slCameraGroup2) + ") "



                #section3
                if ddResultCameraFocalLength == "Not set" and ddResultCameraFocus == "Not set":
                    CameraResult3 = ""
                elif ddResultCameraFocalLength != "Not set" and ddResultCameraFocus != "Not set":
                    ShotFocus = ""
                    ShotFocalLength = ""
                    if ddResultCameraFocus == "Random":
                        ShotFocus = random.choice(RandomFromCameras("CameraFocus"))
                    elif ddResultCameraFocus == "Random From Favs":
                        ShotFocus = random.choice(RandomFavFromCameras("CameraFocus"))
                    else:
                        ShotFocus = ddResultCameraFocus.replace("*", "")
                    if ddResultCameraFocalLength == "Random":
                        ShotFocalLength = random.choice(RandomFromCameras("CameraFocalLength"))
                    elif ddResultCameraFocalLength == "Random From Favs":
                        ShotFocalLength = random.choice(RandomFavFromCameras("CameraFocalLength"))
                    else:
                        ShotFocalLength = ddResultCameraFocalLength.replace("*", "")
                    CameraResult3 = ", (" + ShotFocus + ", " + ShotFocalLength + ":" + str(slCameraGroup3) + ") "

                elif ddResultCameraFocalLength == "Not set":
                    if ddResultCameraFocus == "Random":
                        CameraResult3 = ", (" + random.choice(
                            RandomFromCameras("CameraFocus")) + ":" + str(slCameraGroup3) + ") "
                    elif ddResultCameraFocus == "Random From Favs":
                        CameraResult3 = ", (" + random.choice(
                            RandomFavFromCameras("CameraFocus")) + ":" + str(slCameraGroup3) + ") "
                    else:
                        CameraResult3 = ", (" + ddResultCameraFocus.replace("*", "") + \
                                        ":" + str(slCameraGroup3) + ") "
                elif ddResultCameraFocus == "Not set":
                    if ddResultCameraFocalLength == "Random":
                        CameraResult3 = ", (" + random.choice(
                            RandomFromCameras("CameraFocalLength")) + ":" + str(slCameraGroup3) + ") "
                    elif ddResultCameraFocalLength == "Random From Favs":
                        CameraResult3 = ", (" + random.choice(
                            RandomFavFromCameras("CameraFocalLength")) + ":" + str(slCameraGroup3) + ") "
                    else:
                        CameraResult3 = ", (" + ddResultCameraFocalLength.replace("*", "") + \
                                        ":" + str(slCameraGroup3) + ") "


                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                #artists
                #ddArtistSingle,
                #ddArtistSimilar,
                #slArtistGroupStrength,
                #ArtistResult
                if ddArtistSimilar == "Not set" and ddArtistSingle == "Not set":
                    ArtistResult = ""
                elif ddArtistSimilar != "Not set" and ddArtistSingle != "Not set":
                    SingleArtist = ""
                    SimilarArtist = ""
                    if ddArtistSingle == "Random":
                        SingleArtist = random.choice(RandomFromArtist("Artists"))
                    elif ddArtistSingle == "Random From Favs":
                        SingleArtist = random.choice(RandomFavFromArtists("Artists"))
                    else:
                        SingleArtist = ddArtistSingle.replace("*", "")
                    if ddArtistSimilar == "Random":
                        SimilarArtist = random.choice(RandomFromArtist("ArtistTheme"))
                    elif ddArtistSimilar == "Random From Favs":
                        SimilarArtist = random.choice(RandomFavFromArtists("ArtistTheme"))
                    else:
                        SimilarArtist = ddArtistSimilar.replace("*", "")
                    ArtistResult = ", (" + SingleArtist + ", " + SimilarArtist + ":" + str(slArtistGroupStrength) + ") "

                elif ddArtistSimilar == "Not set":
                    if ddArtistSingle == "Random":
                        ArtistResult = ", (" + random.choice(
                            RandomFromArtist("Artists")) + ":" + str(slArtistGroupStrength) + ") "
                    elif ddArtistSingle == "Random From Favs":
                        ArtistResult = ", (" + random.choice(
                            RandomFavFromArtists("Artists")) + ":" + str(slArtistGroupStrength) + ") "
                    else:
                        ArtistResult = ", (" + ddArtistSingle.replace("*", "") + \
                                        ":" + str(slArtistGroupStrength) + ") "
                elif ddArtistSingle == "Not set":
                    if ddArtistSimilar == "Random":
                        ArtistResult = ", (" + random.choice(
                            RandomFromArtist("ArtistTheme")) + ":" + str(slArtistGroupStrength) + ") "
                    elif ddArtistSimilar == "Random From Favs":
                        ArtistResult = ", (" + random.choice(
                            RandomFavFromArtists("ArtistTheme")) + ":" + str(slArtistGroupStrength) + ") "
                    else:
                        ArtistResult = ", (" + ddArtistSimilar.replace("*", "") + \
                                        ":" + str(slArtistGroupStrength) + ") "
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                # Pick the color tone
                if ddColorTone != "Not set":
                    if ddColorTone == "Random":
                        FinalResultMood = random.choice(RandomFromColors("ColorTones"))
                    elif ddColorTone == "Random From Favs":
                        FinalResultMood = random.choice(RandomFavFromColors("ColorTones"))
                    else:
                        FinalResultMood = ddColorTone
                #color scheme
                if ddColorScheme!= "Not set":
                    if ddColorTone == "Not set":
                        if ddColorScheme == "Random":
                            FinalResultColor = ",(" + random.choice(RandomFromColors("ColorSchemes")) + \
                                ":" + str(slResultColorStrength) + ") "
                        elif ddColorScheme == "Random From Favs":
                            FinalResultColor = ",(" + random.choice(RandomFavFromColors("ColorSchemes")) + \
                                ":" + str(slResultColorStrength) + ") "
                        else:
                            FinalResultColor = ",(" + ddColorScheme + \
                                ":" + str(slResultColorStrength) + ") "
                    else:
                        if ddColorScheme == "Random":
                            FinalResultColor = ",(" + FinalResultMood + ", " + random.choice(RandomFromColors("ColorSchemes")) + \
                                ":" + str(slResultColorStrength) + ") "
                        elif ddColorScheme == "Random From Favs":
                            FinalResultColor = ",(" + FinalResultMood + ", " + random.choice(RandomFavFromColors("ColorSchemes")) + \
                                ":" + str(slResultColorStrength) + ") "
                        else:
                            FinalResultColor = ",(" + FinalResultMood + ", " + ddColorScheme + \
                                ":" + str(slResultColorStrength) + ") "
                else:
                    if ddColorTone != "Not set":
                        FinalResultColor = ",(" + FinalResultMood + \
                                    ":" + str(slResultColorStrength) + ") "
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                # If present, add batch element, otherwise remove that reference
                TempText = ""
                if LineCount > 0:
                    if len(BatchLines[CurrentChoice % LineCount]) > 0:
                        TempText = BatchLines[CurrentChoice % LineCount]

                #TempText = copy_p.prompt.replace("[X]", TempText)
                TempText = p.prompt.replace("[X]", TempText)

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                # If present, add random element, otherwise remove that reference
                if len(RandomLinesA) > 0:
                    TempText = TempText.replace(
                        "[A]", random.choice(RandomLinesA))
                else:
                    TempText = TempText.replace("[A]", "")

                if len(RandomLinesB) > 0:
                    TempText = TempText.replace(
                        "[B]", random.choice(RandomLinesB))
                else:
                    TempText = TempText.replace("[B]", "")

                if len(RandomLinesC) > 0:
                    TempText = TempText.replace(
                        "[C]", random.choice(RandomLinesC))
                else:
                    TempText = TempText.replace("[C]", "")

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                # Colors
               

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                print("FC "+ FinalConcept + " MT " + MainType + " CR1 " + CameraResult1 + " CR2 " + CameraResult2 + " CR3 " + CameraResult3)
                print("ArtistResult " + ArtistResult + " AllMovements " + AllMovements + " FinalResultColor " + FinalResultColor)
                # If main prompt isn't empty...
                
                if MainType !="":
                    TypeFront =  MainType + ", "


                # Our main prompt composed of all the selected elements
                MainPositive = TypeFront + TempText

                if CameraResult1 != "":
                    MainPositive = MainPositive + CameraResult1
                if CameraResult2 != "":
                    MainPositive = MainPositive + CameraResult2
                if CameraResult3 != "":
                    MainPositive = MainPositive + CameraResult3
                if ArtistResult != "":
                    MainPositive = MainPositive + ArtistResult
                if AllMovements != "":
                    MainPositive = MainPositive + AllMovements
                if FinalResultColor != "":
                    MainPositive = MainPositive + FinalResultColor

                
                if cbMediumPositives == True:
                    MainPositive = MainPositive + ", " + TypePositives

                if FinalConcept != "":
                    MainPositive = MainPositive + ", " + FinalConcept

                MainPositive = MainPositive.replace(",,", ",")
                #MainNegative = copy_p.negative_prompt
                MainNegative = p.negative_prompt
                
                if cbMediumNegatives == True:
                    MainNegative = MainNegative + ", " + TypeNegatives

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                SubCurrentChoice = 0

                for z in range(SubCycleCount):
                    # Copy of the main prompt module to make batches, I guess...
                    copy_p = copy.copy(p)

                    if copy_p.seed != -1:  # and 'p.seed' in locals():
                        copy_p.seed += SeedStep

                    SubTempText = ""
                    if SubLineCount > 0:
                        if len(SubBatchLines[SubCurrentChoice % SubLineCount]) > 0:
                            SubTempText = SubBatchLines[SubCurrentChoice % SubLineCount]

                    TempText = MainPositive.replace("[Y]", SubTempText)

                    TempText = TempText.replace("[xs]", str(random.randrange(100000,999999,1)))
                    TempText = TempText.replace("[XS]", str(random.randrange(100000,999999,1)))                    

                    TempText = TempText.replace("[s]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)))
                    TempText = TempText.replace("[S]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)))
                    
                    TempText = TempText.replace("[m]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)))
                    TempText = TempText.replace("[M]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)))
                    
                    TempText = TempText.replace("[l]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)) + " " + ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)))
                    TempText = TempText.replace("[L]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)) + " " + ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=5)))
                    
                    TempText = TempText.replace("[xl]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)) + " " + ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)))
                    TempText = TempText.replace("[XL]", ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)) + " " + ''.join(random.choices("0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ", k=10)))

                    # Clean up positive prompt
                    TempText = " ".join(TempText.split())
                    TempText = TempText.replace(",,", ",")
                    TempText = TempText.replace(" ,", ",")
                    TempText = TempText.replace(",", ",")
                    TempText = TempText.replace("( ", "(")
                    TempText = TempText.replace(" )", ")")
                    TempText = TempText.strip(",")
                    TempText = TempText.strip()

                    copy_p.prompt = TempText

                    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                    # Clean up negative prompt
                    TempText = MainNegative + \
                        AlwaysBad

                    TempText = " ".join(TempText.split())
                    TempText = " ".join(TempText.split())
                    TempText = TempText.replace(",,", ",")
                    TempText = TempText.replace(" ,", ",")
                    TempText = TempText.replace(",", ",")
                    TempText = TempText.replace("( ", "(")
                    TempText = TempText.replace(" )", ")")
                    TempText = TempText.strip(",")
                    TempText = TempText.strip()

                    copy_p.negative_prompt = TempText

                    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                    # Add information in command prompt window and process the image

                    print(f"\n\n[Prompt {x+1}/{MainJobCount}][Iteration {y+1}/{SubIterationCount}][SubPrompt {z}/{SubLineCount}][Seed {int(copy_p.seed)}] >>> Positives <<< {copy_p.prompt} >>> Negatives <<< {copy_p.negative_prompt}\n")

                    proc = process_images(copy_p)
                    infotexts += proc.infotexts
                    images += proc.images
                    seeds.append(proc.seed)
                    prompts.append(proc.prompt)

                    SubCurrentChoice += 1

                    if cbIncreaseSeed == True:
                        SeedStep += 1

            CurrentChoice += 1

        p.batch_size = MainJobCount
        p.n_iter = SubIterationCount

        return Processed(p=p, images_list=images, seed=p.seed, all_seeds=seeds, all_prompts=prompts, info=infotexts[0],
                         infotexts=infotexts)
