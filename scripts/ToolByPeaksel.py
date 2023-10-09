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



# edit_icon = "../Icons/edit.png" FIX

# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
# directories

# General Tab
BeautifiersDir          = os.path.join(scripts.basedir(), f"Variables\\General\\General\\Beautifiers.txt")
DetailsDir              = os.path.join(scripts.basedir(), f"Variables\\General\\General\\details.txt")
MediumsDir              = os.path.join(scripts.basedir(), f"Variables\\General\\General\\Mediums\\MediumType.txt")
MediumsSubDir           = os.path.join(scripts.basedir(), f"Variables\\General\\General\\Mediums\\SubMediums\\")

NegativesDir            = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativetags.txt")
NegativesGeneralDir     = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativetags\\general.txt")
NegativesBWDir          = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativetags\\b&w.txt")
NegativesCharacterDir   = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativetags\\characternegative.txt")
NegativeEmbeddingsCPDir = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativeembeddings\\checkpointspecific.txt")
NegativeEmbeddingsGNDir = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativeembeddings\\generalnegativeembeddings.txt")
NegativeEmbeddingsHHDir = os.path.join(scripts.basedir(), f"Variables\\General\\negatives\\negativeembeddings\\handshelpers.txt")

StyleEmbeddingDir  = os.path.join(scripts.basedir(), f"Variables\\General\\style\\styleembedding.txt")
StyleLoraDir       = os.path.join(scripts.basedir(), f"Variables\\General\\style\\stylelora.txt")
StyleEMBDir        = os.path.join(scripts.basedir(), f"Variables\\General\\style\\styleembedding.txt")
StyleDir           = os.path.join(scripts.basedir(), f"Variables\\General\\style\\generalstyle.txt")
StyleGameDir       = os.path.join(scripts.basedir(), f"Variables\\General\\style\\styleofvideogame.txt")
ColorsTonesDir     = os.path.join(scripts.basedir(), f"Variables\\General\\style\\Colors\\ColorTones.txt")
ColorsSchemesDir   = os.path.join(scripts.basedir(), f"Variables\\General\\style\\Colors\\ColorSchemes.txt")
ArtistSingleDir    = os.path.join(scripts.basedir(), f"Variables\\General\\style\\Artists\\Artists.txt")
ArtistThemeDir     = os.path.join(scripts.basedir(), f"Variables\\General\\style\\Artists\\artisttheme.txt")
MaterialDir        = os.path.join(scripts.basedir(), f"Variables\\General\\style\\material\\materials.txt")
MaterialSubDir     = os.path.join(scripts.basedir(), f"Variables\\General\\style\\material\\submenus\\")

SeasonDir          = os.path.join(scripts.basedir(), f"Variables\\General\\lighting\\seasonoftheyear.txt")
HolidayDir         = os.path.join(scripts.basedir(), f"Variables\\General\\lighting\\exactholiday.txt")
LightingDir        = os.path.join(scripts.basedir(), f"Variables\\General\\lighting\\lighting.txt")
LightingSubDir     = os.path.join(scripts.basedir(), f"Variables\\General\\lighting\\submenus\\")
LightingEffectDir  = os.path.join(scripts.basedir(), f"Variables\\General\\lighting\\lightingeffects.txt")

CameraSettingsDir  = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\")
CameraBrandDir     = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraBrand.txt")
CameraFilmSizeDir  = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraFilmSize.txt")
CameraFocalLenDir  = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraFocalLength.txt")
CameraFocusDir     = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraFocus.txt")
CameraShotTypeDir  = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraShotType.txt")
CameraShotAngleDir = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\CameraShotAngle.txt")
PhotographyTypeDir = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\photographytype.txt")
PhotographersDir   = os.path.join(scripts.basedir(), f"Variables\\General\\Camera\\photographers\\")


#Female Character  General 
ContentRatingDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\contentrating.txt")
BeautyDescriptorDir    = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\beautydescriptor.txt")
FemaleTypeDir          = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\femaletype.txt")
SpecificPersonDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\submenus\\")
GoddessTypeDir         = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\goddess.txt")
GoddessDir             = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\mythology\\")
EmbeddingDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\femaleembedding.txt")
LoraDir                = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\lorafemale.txt")
OriginOrNationalityDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\originornationality.txt")
SkinColorDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\skincolor.txt")
BodyViewDir            = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\bodyview.txt")
CameraAngleDir         = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\bodyangle.txt")
CameraFFocusDir        = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\cameraFocus.txt")
LookingWhereDir        = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\lookingwhere.txt")

# Female Character  Head
HairColorDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\HairColor.txt")
HairCutDir        = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\HairCut.txt")
EyeColorDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\EyeColor.txt")
EyeShapeDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\EyeShape.txt")
FaceShapeDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\FaceShape.txt")
FaceExpressionDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\FaceExpression.txt")
EyeBrowsDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\eyebrows.txt")
ChinDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\chin.txt")
NoseDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\nose.txt")
LipsDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\face\\lips.txt")

# Female Character  Head Accessories 
HairAccessoryDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\hairaccessory.txt")
AnimalEarsDir    = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\animalears.txt")
EarringsDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\earrings.txt")
NecklessDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\neckless.txt")
HatDir           = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\hat.txt")
GlassesDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\head\\submenus\\glasses.txt")

QuickBackGroundDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\general\\quickbackground.txt")

# Female Character Body
BodyTypeDir         = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\bodytype.txt")
AgeDir              = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\age.txt")
SkinDir             = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\skin.txt")
BreastSizeDir       = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\breastssize.txt")
BreastDescriptorDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\breastsdescriptor.txt")
AssSizeDir          = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\asssize.txt")
AssDescriptorDir    = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\assdescriptor.txt")
HipsDir             = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\hips.txt")
LegsDescriptorDir   = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\body\\legs.txt")

WardrobeDir         = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\wardrobe\\wardrobe.txt")
WardrobeSubDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\wardrobe\\wardrobe\\")

FootwearDir         = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\footwear\\footware.txt")
FootwearSubDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\footwear\\footware\\")

# Female Character RPG
FemaleBodyArmorDir          = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\fullbodyarmor.txt")
FemaleHeadProtectionDir     = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\headprotection.txt")
FemaleNeckProtectionDir     = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\neckprotection.txt")
FemaleShoulderProtectionDir = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\shouldersprotection.txt")
FemaleTorsoProtectionDir    = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\torsoprotection.txt")
FemaleLegProtectionDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\legsprotection.txt")
FemaleGroinProtectionDir    = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\groinprotection.txt")
FemaleWeaponDir             = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\femaleweapon.txt")
FemaleWeaponSubmenuDir      = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\weapons\\")
FemaleShieldDir             = os.path.join(scripts.basedir(),f"Variables\\FemaleCharacter\\RPG\\handheldshield.txt")

 
# Male Character GENERAL 
MaleContentRatingDir       = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\malecontentrating.txt")
MaleBeautifiersDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\beautifiers.txt")
MaleTypeDir                = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\maletype.txt")
MaleGodTypeDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\gods.txt")
MaleGodDir                 = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\mythology\\")
MaleSubTypeDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\submenus\\")
MaleEmbeddingsDir          = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\maleembedding.txt")
MaleLoraDir                = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\loramale.txt")
MaleOriginOrNationalityDir = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\originornationality.txt")
MaleSkinColorDir           = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\skincolor.txt")
MaleBodyViewDir            = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\bodyview.txt")
MaleBodyAngleDir           = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\bodyangle.txt")
MaleLookingWhereDir        = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\lookingwhere.txt")
MaleCameraFocusDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\malecamerafocus.txt")

# Male Character BODY
MaleBodyTypeDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\body\\malebodytype.txt")
MaleBodyHeightDir       = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\body\\malebodyheight.txt")
MaleAgeDir              = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\body\\maleage.txt")      
MaleSkinDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\body\\maleskin.txt")

MaleWardrobeDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\wardrobe\\wardrobe.txt")
MaleWardorbeSubDir      = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\wardrobe\\submenus\\")

MaleFootwearDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\footwear\\footwear.txt")
MaleFootwearSubDir      = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\footwear\\submenus\\")


# Male Character HEAD
MaleFaceShapeDir        = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\faceshape.txt")
MaleFaceExpressionDir   = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\faceexpression.txt")
MaleHairColorDir        = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\malehaircolor.txt")
MaleHairCutDir          = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\malehaircut.txt")
MaleEyeColorDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\eyecolor.txt")
MaleEyeShapeDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\eyeshape.txt")
MaleEyeBrowsDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\eyebrows.txt")
MaleGlassesDir          = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\maleglasses.txt")
MaleNoseDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\nose.txt")
MaleChinDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\chin.txt")
MaleMustacheDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\mustache.txt")
MaleBeardDir            = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\beardstyle.txt")
MaleHeadWearDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\maleheadwear.txt")
MaleNecklessDir         = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\head\\maleneckless.txt")

MaleQuickBackGroundDir  = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\general\\quickbackground.txt")

# Male Character RPG
MaleBodyArmorDir          = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\fullbodyarmor.txt")
MaleHeadProtectionDir     = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\headprotection.txt")
MaleNeckProtectionDir     = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\neckprotection.txt")
MaleShoulderProtectionDir = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\shouldersprotection.txt")
MaleTorsoProtectionDir    = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\torsoprotection.txt")
MaleLegProtectionDir      = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\legsprotection.txt")
MaleGroinProtectionDir    = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\groinprotection.txt")
MaleWeaponDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\maleweapon.txt")
MaleWeaponSubmenuDir      = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\weapons\\")
MaleShieldDir             = os.path.join(scripts.basedir(),f"Variables\\MaleCharacter\\RPG\\handheldshield.txt")



# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
# Creating a list of directories so we can extract values from specific files
dirsList = []

def addtoDirs(dir):
    global dirsList 
    dirsList.append(dir)

addtoDirs(MediumsDir);addtoDirs(MediumsSubDir);addtoDirs(BeautifiersDir);addtoDirs(StyleDir);addtoDirs(StyleGameDir);addtoDirs(ColorsTonesDir);addtoDirs(DetailsDir);addtoDirs(NegativesDir);addtoDirs(NegativesGeneralDir);addtoDirs(NegativesBWDir);addtoDirs(NegativesCharacterDir)
addtoDirs(SeasonDir);addtoDirs(HolidayDir);addtoDirs(LightingDir);addtoDirs(LightingSubDir);addtoDirs(LightingEffectDir);addtoDirs(MaterialDir);addtoDirs(MaterialSubDir);addtoDirs(StyleLoraDir);addtoDirs(StyleEMBDir);addtoDirs(StyleEmbeddingDir)
addtoDirs(ColorsSchemesDir);addtoDirs(ArtistSingleDir);addtoDirs(ArtistThemeDir);addtoDirs(CameraSettingsDir);addtoDirs(PhotographyTypeDir);addtoDirs(PhotographersDir);addtoDirs(HairColorDir)
addtoDirs(CameraBrandDir);addtoDirs(CameraShotAngleDir);addtoDirs(CameraShotTypeDir);addtoDirs(CameraFilmSizeDir);addtoDirs(CameraFocalLenDir);addtoDirs(CameraFocusDir)
addtoDirs(HairCutDir);addtoDirs(EyeColorDir);addtoDirs(EyeShapeDir);addtoDirs(FaceShapeDir)
addtoDirs(FaceExpressionDir);addtoDirs(EyeBrowsDir);addtoDirs(ChinDir);addtoDirs(NoseDir);addtoDirs(LipsDir)
addtoDirs(LookingWhereDir);addtoDirs(ContentRatingDir);addtoDirs(BeautyDescriptorDir);addtoDirs(CameraFFocusDir)
addtoDirs(FemaleTypeDir);addtoDirs(SpecificPersonDir);addtoDirs(LoraDir);addtoDirs(EmbeddingDir);addtoDirs(AgeDir);addtoDirs(OriginOrNationalityDir)
addtoDirs(SkinColorDir);addtoDirs(BodyViewDir);addtoDirs(CameraAngleDir);addtoDirs(HairAccessoryDir);addtoDirs(AnimalEarsDir);addtoDirs(EarringsDir);addtoDirs(NecklessDir)
addtoDirs(HatDir);addtoDirs(GlassesDir);addtoDirs(QuickBackGroundDir);addtoDirs(BodyTypeDir);addtoDirs(SkinDir);addtoDirs(BreastSizeDir);addtoDirs(BreastDescriptorDir);addtoDirs(AssSizeDir);addtoDirs(AssDescriptorDir)
addtoDirs(HipsDir);addtoDirs(LegsDescriptorDir);addtoDirs(WardrobeDir);addtoDirs(FootwearDir);addtoDirs(WardrobeSubDir);addtoDirs(FootwearSubDir)
addtoDirs(MaleContentRatingDir);addtoDirs(MaleBeautifiersDir);addtoDirs(MaleTypeDir);addtoDirs(MaleSubTypeDir);addtoDirs(MaleEmbeddingsDir);addtoDirs(MaleLoraDir)
addtoDirs(MaleOriginOrNationalityDir);addtoDirs(MaleSkinColorDir);addtoDirs(MaleBodyViewDir);addtoDirs(MaleBodyAngleDir);addtoDirs(MaleLookingWhereDir);addtoDirs(MaleCameraFocusDir)
addtoDirs(MaleBodyTypeDir);addtoDirs(MaleBodyHeightDir);addtoDirs(MaleAgeDir);addtoDirs(MaleSkinDir);addtoDirs(MaleWardrobeDir);addtoDirs(MaleWardorbeSubDir);addtoDirs(MaleFootwearDir);addtoDirs(MaleFootwearSubDir)
addtoDirs(MaleFaceShapeDir);addtoDirs(MaleFaceExpressionDir);addtoDirs(MaleHairColorDir);addtoDirs(MaleHairCutDir);addtoDirs(MaleEyeColorDir);addtoDirs(MaleEyeShapeDir)
addtoDirs(MaleEyeBrowsDir);addtoDirs(MaleGlassesDir);addtoDirs(MaleNoseDir);addtoDirs(MaleChinDir);addtoDirs(MaleMustacheDir);addtoDirs(MaleBeardDir);addtoDirs(MaleHeadWearDir);addtoDirs(MaleNecklessDir);addtoDirs(MaleQuickBackGroundDir)
addtoDirs(MaleBodyArmorDir);addtoDirs(MaleHeadProtectionDir);addtoDirs(MaleShoulderProtectionDir);addtoDirs(MaleTorsoProtectionDir);addtoDirs(MaleNeckProtectionDir);addtoDirs(MaleLegProtectionDir);addtoDirs(MaleGroinProtectionDir);addtoDirs(MaleWeaponDir)
addtoDirs(MaleWeaponSubmenuDir);addtoDirs(MaleShieldDir);addtoDirs(FemaleBodyArmorDir);addtoDirs(FemaleHeadProtectionDir);addtoDirs(FemaleShoulderProtectionDir);addtoDirs(FemaleTorsoProtectionDir);addtoDirs(FemaleNeckProtectionDir);addtoDirs(FemaleLegProtectionDir);addtoDirs(FemaleGroinProtectionDir);addtoDirs(FemaleWeaponDir)
addtoDirs(FemaleWeaponSubmenuDir);addtoDirs(FemaleShieldDir);addtoDirs(GoddessTypeDir);addtoDirs(GoddessDir);addtoDirs(MaleGodDir);addtoDirs(MaleGodTypeDir)
# =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

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
 

# Functions for merging / formating  inputs in the same row into a single output  

# 1 Field + slider
def Combine_Field_With_Slider(ddFirst,slider,FirstName,FirstDir,FirstPositives,FirstNegatives,FirstResult):

    if ddFirst != "Not set":
        if ddFirst == "Random":
            FirstName = random.choice(RandomFromFile(FirstDir,False))
            if (slider == 1.0):
                FirstResult = FirstName.replace("*","") + " "
            else :
                FirstResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,False)
        elif ddFirst == "Random From Favs":
            FirstName = random.choice(RandomFromFile(FirstDir,True))
            if (slider == 1.0):
                FirstResult = FirstName.replace("*","") + " "
            else :
                FirstResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
        else:
            FirstName = ddFirst.replace("*","")
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
            if (slider == 1.0):
                FirstResult = FirstName  + " "
            else :    
                FirstResult =  " (" + FirstName + ":" + str(slider) + ") " 

    return FirstName,FirstPositives,FirstNegatives,FirstResult,slider         

# 2 Fields + slider 
def Combine_Fields_With_Slider(ddFirst,ddSeccond,slider,FirstPositives,FirstNegatives,SeccondPositives,SeccondNegatives,FirstName,SeccondName,FirstResult,FinalResult,FirstDir,SeccondDir):
    
    # First Field
    if ddFirst != "Not set":
        if ddFirst == "Random":
            FirstName = random.choice(RandomFromFile(FirstDir,False))
            if (slider == 1.0):
                FirstResult = FirstName.replace("*","") + " "
            else :
                FirstResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
        elif ddFirst == "Random From Favs":
            FirstName = RandomFromFile(FirstDir,True)
            if (FirstName == []):
                FirstName = random.choice(RandomFromFile(FirstDir,False))
            else :
                FirstName = random.choice(RandomFromFile(FirstDir,True))
            if (slider == 1.0):
                FirstResult = FirstName.replace("*","") + " "
            else :
                FirstResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
        else:
            FirstName = ddFirst.replace("*","") 
            FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
            FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
            if (slider == 1.0):
                FinalResult = FirstName + " "
            else :
                FirstResult =  " (" + FirstName + ":" + str(slider) + ") "
    # Seccond
    if ddSeccond != "Not set":
        if ddFirst == "Not set":
            if ddSeccond == "Random":
                SeccondName = random.choice(RandomFromFile(SeccondDir,False))
                if (slider == 1.0):
                    FinalResult = SeccondName.replace("*","") + " "
                else :
                    FinalResult = " (" + ddSeccond.replace("*","") + ":" + str(slider) + ") "
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
            elif ddSeccond == "Random From Favs":
                SeccondName = random.choice(RandomFromFile(SeccondDir,True))
                if (slider == 1.0):
                    FinalResult = SeccondName.replace("*","") + " "
                else :
                    FinalResult = " (" + ddSeccond.replace("*","") + ":" + str(slider) + ") "
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
            else:
                SeccondName = ddSeccond.replace("*","")
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
                if (slider == 1.0):
                    FinalResult = SeccondName + " "
                else :
                    FinalResult = " (" + SeccondName + ":" + str(slider) + ") "
        # Female Type && Specific Person       
        else:
            if ddSeccond == "Random":
                SeccondName = random.choice(RandomFromFile(SeccondDir,False))
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
                if (slider == 1.0):
                    FinalResult = SeccondName + ", " + FirstName.replace("*","") + " "
                else : 
                    FinalResult = "(" + SeccondName + ", " + FirstName.replace("*","") + ":" + str(slider) + ") "
            elif ddSeccond == "Random From Favs":
                SeccondName = random.choice(RandomFromFile(SeccondDir,True))
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
                if (slider == 1.0):
                    FinalResult = SeccondName + ", " + FirstName.replace("*","") + " "
                else : 
                    FinalResult = "(" + SeccondName + ", " + FirstName.replace("*","") + ":" + str(slider) + ") "  
            else:
                SeccondName = ddSeccond.replace("*","")
                SeccondPositives = GetPromptsFromFile(SeccondDir,SeccondName,True)
                SeccondNegatives = GetPromptsFromFile(SeccondDir,SeccondName,False)
                if (slider == 1.0):
                    FinalResult = SeccondName + ", " + FirstName.replace("*","") + " "
                else : 
                    FinalResult = "(" + SeccondName + ", " + FirstName.replace("*","") + ":" + str(slider) + ") "
    else:
        if ddFirst != "Not set":
            if (slider == 1.0):
                FinalResult = FirstName.replace("*","") + " "
            else :
                FinalResult = "(" + FirstName.replace("*","") + ":" + str(slider) + ") "

   
    return FirstName, SeccondName, FirstPositives, FirstNegatives, SeccondPositives, SeccondNegatives, FirstResult, FinalResult, slider

# Field + SubField + slider
def Combine_SubFields_With_Slider(ddFirst,ddSeccond,slider,FirstPositives,FirstNegatives,SeccondPositives,SeccondNegatives,FirstName,SeccondName,FirstResult,FinalResult,FirstDir,SeccondDir):
         
        # Wardrobe && SubType
        if(ddSeccond == "Disabled" or ddSeccond == "Not set"):
             if ddFirst != "" and ddFirst != "Not set":
                 # If it is random, give it a random value
                 if ddFirst == "Random":
                     FirstName = random.choice(RandomFromFile(FirstDir,False))
                     if (slider == 1):
                         FinalResult = FirstName.replace("*","") + " "
                     else :
                         FinalResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
                     FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
                     FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
                 elif ddFirst == "Random From Favs":
                     FirstName = random.choice(RandomFromFile(FirstDir,True))
                     if (slider == 1):
                         FinalResult = FirstName.replace("*","") + " "
                     else :
                         FinalResult = " (" + FirstName.replace("*","") + ":" + str(slider) + ") "
                     FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
                     FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
                 # otherwise use the selected value
                 else:
                     FirstName = ddFirst.replace("*","")
                     if (slider == 1):
                         FinalResult = FirstName + " "
                     else :
                         FinalResult = " (" + FirstName + ":" + str(slider) + ") "
                     FirstPositives = GetPromptsFromFile(FirstDir,FirstName,True)
                     FirstNegatives = GetPromptsFromFile(FirstDir,FirstName,False)
        else:
             if ddSeccond != "" and ddSeccond != "Not set":
                 if ddSeccond == "Random":
                     FirstName = ddFirst.replace("*","")
                     SeccondName = random.choice(RandomFromSubFile(SeccondDir,FirstName,False))
                     if (slider == 1):
                         FinalResult = SeccondName.replace("*","") + " "
                     else :
                         FinalResult = " (" + SeccondName.replace("*","") + ":" + str(slider) + ") "          
                     SeccondPositives = GetPromptsFromFile(SeccondDir,FirstName,True ,SeccondName)
                     SeccondNegatives = GetPromptsFromFile(SeccondDir,FirstName,False,SeccondName)
                 elif ddSeccond == "Random From Favs":
                     FirstName = ddFirst.replace("*","")
                     SeccondName = random.choice(RandomFromSubFile(SeccondDir,FirstName,True))
                     if (slider == 1):
                         FinalResult = SeccondName.replace("*","") + " "
                     else :
                         FinalResult = " (" + SeccondName.replace("*", "") + ":" + str(slider) + ") "
                     SeccondPositives = GetPromptsFromFile(SeccondDir,FirstName,True ,SeccondName)                           
                     SeccondNegatives = GetPromptsFromFile(SeccondDir,FirstName,False,SeccondName)
                 # otherwise use the selected value
                 else:
                     SeccondName = ddSeccond.replace("*","") 
                     FirstName = ddFirst.replace("*","")
                     if (slider == 1):
                         FinalResult = SeccondName + " "
                     else :
                         FinalResult = " (" + SeccondName + ":" + str(slider) + ") "
                     SeccondPositives = GetPromptsFromFile(SeccondDir,FirstName,True ,SeccondName)
                     SeccondNegatives = GetPromptsFromFile(SeccondDir,FirstName,False,SeccondName)

        return FirstName, SeccondName, FirstPositives, FirstNegatives, SeccondPositives, SeccondNegatives, FirstResult, FinalResult, slider
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

# helper - print final prompt
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

# print dropdown values
def ListFromDropDown(drop):
    newList = []
    defList = drop.choices
    for line in defList:
        line = line.replace("*","")
        if(((line != "Not set") and (line != "Random")) and (line != "Random From Favs")):
            newList.append(line)
    return newList


# Values from file -> Dropdown UI element 
def Dropdown_List_From_File(filename,y,addDefaults):

    PromptValues = []
    file1 = open(filename, 'r')
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

# Values from a subfile -> Dropdown element
def Dropdown_List_From_SubFile(filename,subfilename,y,addDefaults):

    PromptValues = []
    file1 = open(filename+str(subfilename).replace("*","")+'.txt', 'r')
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
    
    return gr.Dropdown(PromptValues, label=y, value=PromptValues[0], interactive = False)

# Returns all values from a file (picks random value when called in the UI section ) 
def RandomFromFile(filename,favourites):
    
    randomList = []
    file1 = open(filename, 'r')
    Lines = file1.readlines()
    for line in Lines:
        line = line.strip()
        xNew = line.split(";")
        if (favourites):
            if (xNew[4] == "True"):
                randomList.append(xNew[0])
        else :
            randomList.append(xNew[0])
            
    return randomList

# Returns all values from subfile (we pick random with choice function after calling this)
def RandomFromSubFile(filename,subfilename,favourites):

    randomList = []
    file1 = open(filename + str(subfilename).replace(" ","").replace("a ","")+".txt", 'r')
    Lines = file1.readlines()
    for line in Lines:
            line = line.strip()
            xNew = line.split(";")
            if (favourites):
                if (xNew[4] == "True"):
                    randomList.append(xNew[0])
            else :
                randomList.append(xNew[0])
                
    return randomList


 #artists

# gets positive or negative prompts from files/subfiles 
# positive True -> positive prompts 
# positive False -> negative prompts 
def GetPromptsFromFile(filename,type,positive,subfilename="None"):

    dir = None
    for item in dirsList:
        if filename == item:
            dir = item
            break

    # get positives / negatives   from Type file if subtype isnt selected 

    if subfilename == "None" :

        file1 = open(dir, 'r')
        Lines = file1.readlines()
        atributes = ""
        # Strips the newline character
        for line in Lines:
            line = line.strip()
            xNew = line.split(";")
            if(xNew[0] == str(type).replace("*","").replace("a ","")):
                if (positive):
                    atributes = xNew[2]
                else :
                    atributes = xNew[3]
        return atributes
    
    # else get positives / negatives  from subtype file 
    else :
        if (dir == MediumsSubDir):
            file1 = open(dir + str(type).replace(" ","").replace("*","")+'.txt', 'r')
        else :
            file1 = open(dir + str(type).replace("a ","").replace(" ","").replace("*","")+'.txt', 'r')
        Lines = file1.readlines()
        atributes = ""
        # Strips the newline character
        for line in Lines:
            line = line.strip()
            xNew = line.split(";")
            if(xNew[0] == str(subfilename).replace("*","")):
                if(positive):
                    atributes = xNew[2]
                else :
                    atributes = xNew[3]
        return atributes



# Returns a gradio checkbox element and puts it into a global list of buttons for formating afterwards
buttons = []
def CheckBox(text):
    global buttons 
    button  = gr.Checkbox(value = False, label = text , scale = 2)
    buttons.append(button)
    return button


#refresh specific dropdown menu 
# TO-DO combine all into one   
def RefreshDropDown(name):
    PromptValues = []
    hasFavs = False
    file1 = open(MediumsSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown2(name):
    PromptValues = []
    hasFavs = False
    file1 = open(SpecificPersonDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown3(name):
    PromptValues = []
    hasFavs = False
    file1 = open(WardrobeSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown4(name):
    PromptValues = []
    hasFavs = False
    file1 = open(FootwearSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown5(name):
    PromptValues = []
    hasFavs = False
    file1 = open(MaleSubTypeDir+str(name).replace("a ","").replace(" ","").replace("*","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown6(name):

    PromptValues = []
    hasFavs = False
    file1 = open(MaleWardorbeSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown7(name):
    PromptValues = []
    hasFavs = False
    file1 = open(MaleFootwearSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown8(name):
    PromptValues = []
    hasFavs = False
    file1 = open(MaleWeaponSubmenuDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown9(name):

    PromptValues = []
    hasFavs = False
    file1 = open(FemaleWeaponSubmenuDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown10(name):

    PromptValues = []
    hasFavs = False
    file1 = open(PhotographersDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown11(name):

    PromptValues = []
    hasFavs = False
    file1 = open(LightingSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown12(name):

    PromptValues = []
    hasFavs = False
    file1 = open(MaterialSubDir+str(name).replace("*","").replace("a ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown13(name):

    PromptValues = []
    hasFavs = False
    file1 = open(GoddessDir+str(name).replace("*","").replace("_ ","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)

def RefreshDropDown14(name):

    PromptValues = []
    hasFavs = False
    file1 = open(MaleGodDir+str(name).replace("*","").replace(" ","")+'.txt', 'r')
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
        PromptValues = ["Not set", "Random"] + PromptValues;
    
    if (name == "Not set" or name == "Random"):
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= False)
    else :
        return gr.Dropdown.update(choices=PromptValues, value = PromptValues[0], interactive= True)
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

    # UI 
    # ======================================================================
    def ui(self, is_img2img):

        gr.HTML('<br />')
        # General
        with gr.Tab("General"):

            # General 
            with gr.Column(variant = "panel"):
                with gr.Row(variant = "panel"):    
                    gr.HTML('<h1>General </h1>')
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    #gr.Label(value = "", label = "", visible = "False", interactive = "False", show_label = "False" ,info = "Poruka").style(container = False)
                    resetButton = gr.Button('Reset ALL General', variant = 'stop' , size = "sm")  
            #Beautifiers
                with gr.Row(variant = "panel"):
                    ddBeautifiers = Dropdown_List_From_File(BeautifiersDir, "Beautifiers", True)
                    ddDetails       = Dropdown_List_From_File(DetailsDir,"Details",True)           
                    slBeautifierStrength = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
            #Mediums
                with gr.Row(variant = "panel"):
                    ddMediumType = Dropdown_List_From_File(MediumsDir,"Medium Type", True)
                    ddMediumSubType = Dropdown_List_From_SubFile(MediumsSubDir,ddMediumType,"Submenu", True)
                    ddMediumType.change(RefreshDropDown, ddMediumType, ddMediumSubType)
                    slMediumStrength = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
                    
            # Negatives 
            with gr.Column(variant = "panel"):
                with gr.Row():
                    gr.HTML('<h1>Negatives</h1>')      
                with gr.Row(variant = "panel"):
                    ddNegatives = Dropdown_List_From_File(NegativesDir, "Negatives", True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    gr.HTML('<h1 style="display: none;">a</h1>')          
            
            with gr.Row(variant = "panel"):
                with gr.Column(scale = 1 , min_width = 100):
                    with gr.Row(): 
                        gr.HTML('<h3>General purpose</h3>')
                    with gr.Row():
                        ckbutton2  = gr.Checkbox(value = False, label = "Bad Pictures" , scale = 2)
                    with gr.Row():
                        ckbutton3  = gr.Checkbox(value = False, label = "Bad Artists" , scale = 2)
                    with gr.Row():    
                        ckbutton4  = gr.Checkbox(value = False, label = "Fast Negative v2" , scale = 2)
                    with gr.Row():
                        ckbutton5  = gr.Checkbox(value = False, label = "Concordant" , scale = 2)
                    with gr.Row():
                        ckbutton6  = gr.Checkbox(value = False, label = "Boring Negative (more interesting images)" , scale = 2)
                    with gr.Row():    
                        ckbutton7  = gr.Checkbox(value = False, label = "Bad Dream + UnrealisticDream (for photorealistic images)" , scale = 2)
                    with gr.Row():
                        ckbutton21 = gr.Checkbox(value = False, label = "Deep Negative v1", scale = 2)
                    with gr.Row():
                        ckbutton22 = gr.Checkbox(value = False, label = "Very Bad Image Negative" , scale = 2)
                    with gr.Row():
                        ckbutton23 = gr.Checkbox(value = False, label = "Fast Negative Embedding (+ FastNegativeV2)", scale = 2)
                    with gr.Row():   
                        gr.HTML('<h3>Hands Helpers</h1>')
                    with gr.Row():
                        ckbutton8  = gr.Checkbox(value = False, label = "Bad Hands v5" , scale = 2)
                    with gr.Row():    
                        ckbutton9  = gr.Checkbox(value = False, label = "Bad Hand v4 for Anime Illustration Diffusion" , scale = 2)
                    with gr.Row():
                        ckbutton10 = gr.Checkbox(value = False, label = "Bad Prompt v2" , scale = 2)
                    with gr.Row():
                        ckbutton11 = gr.Checkbox(value = False, label = "Negative Hand" , scale = 2)

                with gr.Column( scale = 1 , min_width = 200):
                    with gr.Row():
                        gr.HTML('<h3>Checkpoint Specific</h1>')
                    with gr.Row():    
                        ckbutton12 = gr.Checkbox(value = False, label = "Anime Style negative embedding for Dreamshaper" , scale = 2)
                    with gr.Row():
                        ckbutton13 = gr.Checkbox(value = False, label = "Bad Dream for Dreamshaper" , scale = 2)
                    with gr.Row():    
                        ckbutton14 = gr.Checkbox(value = False, label = "Bad Picture for Chillout Mix" , scale = 2)
                    with gr.Row():     
                        ckbutton15 = gr.Checkbox(value = False, label = "Negative Embedding for Deliberate" , scale = 2)
                    with gr.Row():
                        ckbutton16 = gr.Checkbox(value = False, label = "Negative Embedding for Realistic Vision" , scale = 2)
                    with gr.Row():    
                        ckbutton17 = gr.Checkbox(value = False, label = "Bad Quality for Waiffu Diffusion 1.5 beta" , scale = 2)
                    with gr.Row():    
                        ckbutton18 = gr.Checkbox(value = False, label = "Negative Embedding for Juggernaut" , scale = 2)
                    with gr.Row():    
                        ckbutton19 = gr.Checkbox(value = False, label = "Beyond Negative for Beyond Reality 2" , scale = 2)
                    with gr.Row():    
                        ckbutton20 = gr.Checkbox(value = False, label = "EasyNegative for Counterfeit v3" , scale = 2)
                    with gr.Row():
                        ckbutton24 = gr.Checkbox(value = False, label = "CyberRealistic Negative" , scale = 2)

                    
            # Style
            with gr.Column(variant = "panel"):
                with gr.Row(variant = "panel"):      
                    gr.HTML('<h1>Style</h1>')
                #Style Lora 
                with gr.Row(variant = "panel"):     
                    ddStyleLora = Dropdown_List_From_File(StyleLoraDir, "Style Lora", True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slStyleLoraStrength = gr.Slider( 0, 2, value=1.0, step=0.05, show_label=False)
                #Style Embedding  
                with gr.Row(variant = "panel"):
                    #ddStyleEMB = Dropdown_List_From_File(StyleEMBDir, "Style Embedding", True)
                    css = """
                    #editButton.lg.secondary.gradio-button.editButton.svelte-1ipelgc {min-width: 30px !important; max-width: 30px !important; padding: 0px !important}
                    #editButton {min-width: 30px !important; max-width: 30px !important; padding: 0px !important} """
                    ddStyleEmbedding = Dropdown_List_From_File(StyleEmbeddingDir,"Style Embedding ",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    #editButton = gr.Button('✏️',size = 'sm', max_width = '25px' , min_width = '25px', elem_id = "editButton", elem_classes = "editButton")
                    #gr.HTML('<button style="display: inline-block; width: 30px; height: 30px; background-color: #3498db; border: none; border-radius: 5px; cursor: pointer; padding: 0;"><img src="{edit_icon}" alt="Icon" style="width: 100%; height: 100%;"></button>')
                    slStyleEmbeddingStrength = gr.Slider( 0, 2, value=1.0, step=0.05, show_label=False)            
                #Style of 
                with gr.Row(variant = "panel"):         
                    ddStyleGeneral   = Dropdown_List_From_File(StyleDir,"Style General",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slStyleGeneralStrength = gr.Slider( 0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Row(variant = "panel"):         
                    ddStyleGame      = Dropdown_List_From_File(StyleGameDir,"Style of Video Game", True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slStyleGameStrength = gr.Slider( 0, 2, value=1.3, step=0.05, show_label=False)             
                #Colors
                with gr.Row(variant = "panel"):         
                    ddColorTone   = Dropdown_List_From_File(ColorsTonesDir,"Color Tone",True)
                    ddColorScheme = Dropdown_List_From_File(ColorsSchemesDir,"Color Scheme", True)
                    slResultColorStrength = gr.Slider( 0, 2, value=1.0, step=0.05, show_label=False)
                # Artists    
                with gr.Row():
                    ddArtistSingle  = Dropdown_List_From_File(ArtistSingleDir, "Artists", True)
                    ddArtistSimilar = Dropdown_List_From_File(ArtistThemeDir, "Artist Theme", True)
                    slArtistGroupStrength = gr.Slider( 0, 2, value=1.0, step=0.05, show_label=False)
                # Material 
                with gr.Row():
                    ddMaterial     = Dropdown_List_From_File(MaterialDir, "Material", True)
                    ddMaterialSub  = Dropdown_List_From_SubFile(MaterialSubDir,ddMaterial, "Submenu", True)                                                                                                                   
                    ddMaterial.change(RefreshDropDown12, ddMaterial, ddMaterialSub)
                    slMaterialStrength = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)

            # Lighting
            with gr.Column(variant="panel"):
                with gr.Row():
                    gr.HTML('<h1>Lighting</h1>')
                with gr.Row():
                    ddSeason   = Dropdown_List_From_File(SeasonDir, "Season", True)
                    ddHoliday  = Dropdown_List_From_File(HolidayDir, "Exact Holiday", True)
                    slSeasonHolidayStrength = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Row():
                    ddLighting     = Dropdown_List_From_File(LightingDir, "Lighting", True)
                    ddLightingSub  = Dropdown_List_From_SubFile(LightingSubDir,ddLighting, "Submenu", True)                                                                                                                   
                    ddLighting.change(RefreshDropDown11, ddLighting, ddLightingSub)
                    slLightingStrength = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
                with gr.Row():
                    ddLightingEffect = Dropdown_List_From_File(LightingEffectDir,"Lighting Effect",True)    
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slLightingEffectStrength = gr.Slider(0, 2, value=1.3, step=0.05,show_label=False) 

            # Camera stuff
            with gr.Column(variant="panel"):
                with gr.Row():
                    gr.HTML('<h1>Camera</h1>')
                with gr.Column(variant="panel"):
                    with gr.Row():
                        randomCameraButton = gr.Button('Random From All')
                        randomFavsCameraButton = gr.Button('Random From Favs')
                        resetCameraButton = gr.Button('Reset All', variant = 'stop')
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddCameraShotType = Dropdown_List_From_File(CameraShotTypeDir, "Camera Shot Type", True)
                        ddCameraShotAngle = Dropdown_List_From_File(CameraShotAngleDir, "Camera Shot Angle", True)
                        slCameraGroup1 = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddCameraBrand = Dropdown_List_From_File(CameraBrandDir, "Camera Brand", True)
                        ddCameraFilmSize = Dropdown_List_From_File(CameraFilmSizeDir, "Camera Film Size", True)
                        slCameraGroup2 = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddCameraFocus = Dropdown_List_From_File(CameraFocusDir, "Camera Focus", True)
                        ddCameraFocalLength = Dropdown_List_From_File(CameraFocalLenDir, "Camera Focal Length", True)
                        slCameraGroup3 = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)
                with gr.Column(variant="panel"):
                    with gr.Row():
                        ddPhotographyType = Dropdown_List_From_File(PhotographyTypeDir, "Photography type", True)
                        ddPhotographers   = Dropdown_List_From_SubFile(PhotographersDir,ddPhotographyType, "Photographers", True)
                        ddPhotographyType.change(RefreshDropDown10, ddPhotographyType, ddPhotographers)
                        slPhotographyStrenght    = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)

            # Variables
            with gr.Column(variant="panel"):
                with gr.Row():
                    gr.HTML('<h1>Variables</h1>')
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


                randomCameraButton.click(random_all_camera,inputs=ddCameraShotType,    outputs=ddCameraShotType)
                randomCameraButton.click(random_all_camera,inputs=ddCameraShotAngle,   outputs=ddCameraShotAngle)
                randomCameraButton.click(random_all_camera,inputs=ddCameraBrand,       outputs=ddCameraBrand)
                randomCameraButton.click(random_all_camera,inputs=ddCameraFilmSize,    outputs=ddCameraFilmSize)
                randomCameraButton.click(random_all_camera,inputs=ddCameraFocus,       outputs=ddCameraFocus)
                randomCameraButton.click(random_all_camera,inputs=ddCameraFocalLength, outputs=ddCameraFocalLength)
                randomCameraButton.click(random_all_camera,inputs=ddPhotographers,           outputs=ddPhotographers)
                randomCameraButton.click(random_all_camera,inputs=ddPhotographyType,         outputs=ddPhotographyType)               

                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraShotType,    outputs=ddCameraShotType)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraShotAngle,   outputs=ddCameraShotAngle)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraBrand,       outputs=ddCameraBrand)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraFilmSize,    outputs=ddCameraFilmSize)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraFocus,       outputs=ddCameraFocus)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddCameraFocalLength, outputs=ddCameraFocalLength)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddPhotographers,           outputs=ddPhotographers)
                randomFavsCameraButton.click(random_all_favs_camera,inputs=ddPhotographyType,         outputs=ddPhotographyType) 

                resetCameraButton.click(reset_all_camera,inputs=ddCameraShotType,    outputs=ddCameraShotType)
                resetCameraButton.click(reset_all_camera,inputs=ddCameraShotAngle,   outputs=ddCameraShotAngle)
                resetCameraButton.click(reset_all_camera,inputs=ddCameraBrand,       outputs=ddCameraBrand)
                resetCameraButton.click(reset_all_camera,inputs=ddCameraFilmSize,    outputs=ddCameraFilmSize)
                resetCameraButton.click(reset_all_camera,inputs=ddCameraFocus,       outputs=ddCameraFocus)
                resetCameraButton.click(reset_all_camera,inputs=ddCameraFocalLength, outputs=ddCameraFocalLength)
                resetCameraButton.click(reset_all_camera,inputs=ddPhotographyType,         outputs=ddPhotographyType)
                resetCameraButton.click(reset_all_camera,inputs=ddPhotographers,           outputs=ddPhotographers)

                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup1, outputs=slCameraGroup1)
                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup2, outputs=slCameraGroup2)
                resetCameraButton.click(reset_all_camera_value,inputs=slCameraGroup3, outputs=slCameraGroup3)
                resetCameraButton.click(reset_all_camera_value,inputs=slPhotographyStrenght, outputs=slPhotographyStrenght)

                resetButton.click(reset_all_camera,inputs=ddBeautifiers     ,outputs=ddBeautifiers)
                resetButton.click(reset_all_camera,inputs=ddDetails         ,outputs=ddDetails)
                resetButton.click(reset_all_camera,inputs=ddMediumType      ,outputs=ddMediumType)
                resetButton.click(reset_all_camera,inputs=ddMediumSubType   ,outputs=ddMediumSubType)
                resetButton.click(reset_all_camera,inputs=ddStyleLora       ,outputs=ddStyleLora)
                resetButton.click(reset_all_camera,inputs=ddStyleEmbedding ,outputs=ddStyleEmbedding)
                resetButton.click(reset_all_camera,inputs=ddStyleGeneral    ,outputs=ddStyleGeneral)
                resetButton.click(reset_all_camera,inputs=ddStyleGame       ,outputs=ddStyleGame)
                resetButton.click(reset_all_camera,inputs=ddSeason          ,outputs=ddSeason)                
                resetButton.click(reset_all_camera,inputs=ddHoliday         ,outputs=ddHoliday)
                resetButton.click(reset_all_camera,inputs=ddLighting        ,outputs=ddLighting)
                resetButton.click(reset_all_camera,inputs=ddLightingSub     ,outputs=ddLightingSub)
                resetButton.click(reset_all_camera,inputs=ddLightingEffect  ,outputs=ddLightingEffect)
                resetButton.click(reset_all_camera,inputs=ddColorScheme     ,outputs=ddColorScheme)
                resetButton.click(reset_all_camera,inputs=ddColorTone       ,outputs=ddColorTone)
                resetButton.click(reset_all_camera,inputs=ddArtistSingle    ,outputs=ddArtistSingle)
                resetButton.click(reset_all_camera,inputs=ddArtistSimilar   ,outputs=ddArtistSimilar)
                resetButton.click(reset_all_camera,inputs=ddMaterial        ,outputs=ddMaterial)
                resetButton.click(reset_all_camera,inputs=ddMaterialSub     ,outputs=ddMaterialSub)
                resetButton.click(reset_all_camera,inputs=ddNegatives       ,outputs=ddNegatives)
                              
        # Female Character
        with gr.Tab("Female Character"):



        # General section
            with gr.Column(variant="panel"):
                with gr.Row(variant="panel"):
                    gr.HTML('<h1>General</h1>') 
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    resetAllButton = gr.Button('Reset ALL  Female Character', variant = 'stop' , size = "sm")


            # Beauty Descriptor  / Content Rating  
                with gr.Row(variant="panel"):
                    ddBeautyDescriptor = Dropdown_List_From_File(BeautyDescriptorDir,"Beauty Descriptor", True)
                    ddContentRating    = Dropdown_List_From_File(ContentRatingDir,"Content Rating", True) 
                    slBeautyStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Female  type  / Submenu     
                with gr.Row(variant="panel"):
                    ddFemaleType     = Dropdown_List_From_File(FemaleTypeDir,"Female Type", True)
                    ddSpecificPerson = Dropdown_List_From_SubFile(SpecificPersonDir,"ghost","Submenu", True)
                    ddFemaleType.change(RefreshDropDown2, ddFemaleType, ddSpecificPerson)
                    slFemaleTypeStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # GoddessType  / Goddess     
                with gr.Row(variant="panel"):
                    ddGoddessType   = Dropdown_List_From_File(GoddessTypeDir,"Goddess", True)
                    ddGoddess       = Dropdown_List_From_SubFile(GoddessDir,ddGoddessType,"Submenu", True)
                    ddGoddessType.change(RefreshDropDown13, ddGoddessType, ddGoddess)
                    slGoddessStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
            # Embedding     
                with gr.Row(variant="panel"):
                    ddEmbedding      = Dropdown_List_From_File(EmbeddingDir,"Embedding", True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slCelebrityEmbedding = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Lora 
                with gr.Row(variant="panel"):
                    ddLora         = Dropdown_List_From_File(LoraDir,"Lora",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slLoraStrenght  = gr.Slider(0,2, value=1.0,step=0.05,show_label=False)   


            # Origin-Nationality / Skin Color    
                with gr.Row(variant="panel"):
                        ddOriginOrNationality = Dropdown_List_From_File(OriginOrNationalityDir,"Origin or Nationality", True)
                #with gr.Column(variant="panel"):
                #        gr.HTML('<p>Skin Color<p>')
                        #gr.HTML('<button type="button">Click Me!</button>')
                        ddSkinColor         = Dropdown_List_From_File(SkinColorDir,"Skin Color", True)
               # with gr.Column(variant="panel"):
                        slOriginColorStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
            

            # Body View / Camera Angle      
                with gr.Row(variant="panel"):
                    ddBodyView    = Dropdown_List_From_File(BodyViewDir,"Body View", True)
                    ddCameraAngle = Dropdown_List_From_File(CameraAngleDir, "Camera Angle", True)
                    slBodyAngleStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)                    

            # Camera focus / Looking Where                         
                with gr.Row(variant="panel"):
                    ddCameraFFocus = Dropdown_List_From_File(CameraFFocusDir,"Camera Focus",True)
                    ddLookingWhere = Dropdown_List_From_File(LookingWhereDir,"Looking Where",True)
                    slCameraLookingWhereStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

        # Body 
            with gr.Column(variant="panel"):
                gr.HTML('<h1>Body</h1>') 

            # Body Type    
                with gr.Row(variant="panel"):
                    ddBodyType      = Dropdown_List_From_File(BodyTypeDir,"Body Type", True)
                    gr.HTML('<h1 style="display: none;">a</h1>') 
                    slBodyTypeStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False) 

            # Age / Skin     
                with gr.Row(variant="panel"):
                    ddAge          = Dropdown_List_From_File(AgeDir,"Age", True)
                    ddSkin         = Dropdown_List_From_File(SkinDir,"Skin", True)
                    slAgeSkinStrenght   = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Breast size / desc     
                with gr.Row(variant="panel"):
                    ddBreastSize       = Dropdown_List_From_File(BreastSizeDir,"Breasts Size", True)
                    ddBreastDesc       = Dropdown_List_From_File(BreastDescriptorDir,"Breasts Descriptor", True)
                    slBreastStrenght   = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Ass size / desc     
                with gr.Row(variant="panel"):
                    ddAssSize       = Dropdown_List_From_File(AssSizeDir,"Ass Size", True)
                    ddAssDesc       = Dropdown_List_From_File(AssDescriptorDir,"Ass Descriptor", True)
                    slAssStrenght   = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Hips / Legs Descriptor     
                with gr.Row(variant="panel"):
                    ddHips               = Dropdown_List_From_File(HipsDir,"Hips", True)
                    ddLegsDesc           = Dropdown_List_From_File(LegsDescriptorDir,"Legs Descriptor", True)
                    slHipsLegsStrenght   = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Wardrobe
                with gr.Row(variant="panel"):
                    ddWardrobe          = Dropdown_List_From_File(WardrobeDir,"Wardrobe", True)
                    ddWardrobeSub       = Dropdown_List_From_SubFile(WardrobeSubDir,ddWardrobe,"Submenu",True)
                    ddWardrobe.change(RefreshDropDown3,ddWardrobe,ddWardrobeSub) 
                    slWardrobeStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Footwear
                with gr.Row(variant="panel"):
                    ddFootwear          = Dropdown_List_From_File(FootwearDir,"Footwear", True)
                    ddFootwearSub       = Dropdown_List_From_SubFile(FootwearSubDir,ddFootwear,"Submenu",True)
                    ddFootwear.change(RefreshDropDown4,ddFootwear,ddFootwearSub) 
                    slFootwearStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

        # Head section

            with gr.Column(variant="panel"):
                gr.HTML('<h1>Head</h1>') 
            # Face                                  
                with gr.Row(variant="panel"):       
                    ddFaceShape      = Dropdown_List_From_File(FaceShapeDir,"Face Shape", True)
                    ddFaceExpression = Dropdown_List_From_File(FaceExpressionDir,"Face Expression",True)
                    slShapeExpressionStrenght = gr.Slider(0, 2, value=1.3, step=0.05, show_label=False)

            # Hair                          
                with gr.Row(variant="panel"):   
                    ddHairColor = Dropdown_List_From_File(HairColorDir,"Hair Color", True)
                    ddHairCut   = Dropdown_List_From_File(HairCutDir,"Haircuts",True)
                    slColorCutStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
         
            # Eyes                                  
                with gr.Row(variant="panel"):
                    ddEyeColor = Dropdown_List_From_File(EyeColorDir,"Eye Color", True)
                    ddEyeShape = Dropdown_List_From_File(EyeShapeDir,"Eye shape",True)
                    slColorShapeStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # EyeBrows / Nose                         
                with gr.Row(variant="panel"):
                    ddEyeBrows = Dropdown_List_From_File(EyeBrowsDir,"EyeBrows", True)
                    ddNose     = Dropdown_List_From_File(NoseDir,"Nose",True)
                    slBrowsNoseStrenght = gr.Slider(0 ,2, value=1.0, step=0.05, show_label=False)

            # Lips / Chin                                
                with gr.Row(variant="panel"):
                    ddLips = Dropdown_List_From_File(LipsDir,"Lips",True)
                    ddChin = Dropdown_List_From_File(ChinDir,"Chin",True)
                    slLipsChinStrenght = gr.Slider(0 ,2, value=1.0, step=0.05, show_label=False)
            
        # Head Acessories
            with gr.Column(variant="panel"):
                gr.HTML('<h1>Head Accessories</h1>') 

            # Hair Accessories  / Animal Ears     
                with gr.Row(variant="panel"):
                    ddHairAccessories  = Dropdown_List_From_File(HairAccessoryDir,"Hair Accessories", True)
                    ddAnimalEars       = Dropdown_List_From_File(AnimalEarsDir,"Animal Ears", True)
                    slHairEarsStrenght = gr.Slider(0, 2, value=1.0, step=0.05,show_label=False)

            # Earrings  / Neckless     
                with gr.Row(variant="panel"):
                    ddEarrings       = Dropdown_List_From_File(EarringsDir,"Earrings", True)
                    ddNeckless       = Dropdown_List_From_File(NecklessDir,"Neckless", True)
                    slEarringsNecklessStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Hat  / Glasses     
                with gr.Row(variant="panel"):
                    ddHat           = Dropdown_List_From_File(HatDir,"Hat", True)
                    ddGlasses       = Dropdown_List_From_File(GlassesDir,"Glasses", True)
                    slHatGlassesStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Quick background 
                with gr.Row(variant="panel"):
                    ddQuickBackGround = Dropdown_List_From_File(QuickBackGroundDir,"Quick Background",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slBackGroundStrenght = gr.Slider(0,2,value=1.0,step=0.05,show_label=False)

        # RPG
            with gr.Column(variant="panel"):
                gr.HTML('<h1>RPG Dress up Corner</h1>') 
            # Full Body Armor 
                with gr.Row(variant="panel"):
                    ddFemaleFullBodyArmor = Dropdown_List_From_File(FemaleBodyArmorDir,"Full Body Armor",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slFemaleFullBodyArmorStrenght = gr.Slider(0,2,value=1.0,step=0.05,show_label=False)

            # Head Protection  / Neck Protection     
                with gr.Row(variant="panel"):
                    ddFemaleHeadArmor       = Dropdown_List_From_File(FemaleHeadProtectionDir,"Head Protection", True)
                    ddFemaleNeckArmor       = Dropdown_List_From_File(FemaleNeckProtectionDir,"Neck Protection", True)
                    slFemaleHeadNeckStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Shoulder Protection / Torso Protection
                with gr.Row(variant="panel"):
                    ddFemaleShoulderArmor    = Dropdown_List_From_File(FemaleShoulderProtectionDir,"Shoulder Protection", True)
                    ddFemaleChestArmor       = Dropdown_List_From_File(FemaleTorsoProtectionDir,"Torso Protection", True)
                    slFemaleShoulderChestStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Legs Protection / Groin Protection
                with gr.Row(variant="panel"):
                    ddFemaleLegArmor     = Dropdown_List_From_File(FemaleLegProtectionDir,"Legs Protection ", True)
                    ddFemaleGroinArmor   = Dropdown_List_From_File(FemaleGroinProtectionDir,"Groin Protection", True)
                    slFemaleLegGroinStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Weapons
                with gr.Row(variant="panel"):
                    ddFemaleWeapons          = Dropdown_List_From_File(FemaleWeaponDir,"Weapons", True)
                    ddFemaleWeaponsSub       = Dropdown_List_From_SubFile(FemaleWeaponSubmenuDir,ddFemaleWeapons,"Submenu",True)
                    ddFemaleWeapons.change(RefreshDropDown9,ddFemaleWeapons,ddFemaleWeaponsSub) 
                    slFemaleWeaponsStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Hand Held Shield
                with gr.Row(variant="panel"):
                    ddFemaleShield = Dropdown_List_From_File(FemaleShieldDir,"Hand held Shield",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slFemaleShield = gr.Slider(0,2,value=1.0,step=0.05,show_label=False)

            resetAllButton.click(reset_all_camera,inputs=ddBeautyDescriptor,    outputs=ddBeautyDescriptor)
            resetAllButton.click(reset_all_camera,inputs=ddContentRating,       outputs=ddContentRating)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleType,          outputs=ddFemaleType)
            resetAllButton.click(reset_all_camera,inputs=ddSpecificPerson,      outputs=ddSpecificPerson)
            resetAllButton.click(reset_all_camera,inputs=ddGoddessType,         outputs=ddGoddessType)
            resetAllButton.click(reset_all_camera,inputs=ddGoddess,             outputs=ddGoddess)
            resetAllButton.click(reset_all_camera,inputs=ddEmbedding,           outputs=ddEmbedding)
            resetAllButton.click(reset_all_camera,inputs=ddLora,                outputs=ddLora)
            resetAllButton.click(reset_all_camera,inputs=ddOriginOrNationality, outputs=ddOriginOrNationality)
            resetAllButton.click(reset_all_camera,inputs=ddSkinColor,           outputs=ddSkinColor)
            resetAllButton.click(reset_all_camera,inputs=ddBodyView,            outputs=ddBodyView)
            resetAllButton.click(reset_all_camera,inputs=ddCameraAngle,         outputs=ddCameraAngle)
            resetAllButton.click(reset_all_camera,inputs=ddLookingWhere,        outputs=ddLookingWhere)
            resetAllButton.click(reset_all_camera,inputs=ddCameraFFocus,        outputs=ddCameraFFocus)
            resetAllButton.click(reset_all_camera,inputs=ddBodyType,            outputs=ddBodyType)
            resetAllButton.click(reset_all_camera,inputs=ddAge,                 outputs=ddAge)
            resetAllButton.click(reset_all_camera,inputs=ddSkin,                outputs=ddSkin)
            resetAllButton.click(reset_all_camera,inputs=ddBreastSize,          outputs=ddBreastSize)
            resetAllButton.click(reset_all_camera,inputs=ddBreastDesc,          outputs=ddBreastDesc)
            resetAllButton.click(reset_all_camera,inputs=ddAssSize,             outputs=ddAssSize)
            resetAllButton.click(reset_all_camera,inputs=ddAssDesc,             outputs=ddAssDesc)    
            resetAllButton.click(reset_all_camera,inputs=ddHips,                outputs=ddHips)    
            resetAllButton.click(reset_all_camera,inputs=ddLegsDesc,            outputs=ddLegsDesc)    
            resetAllButton.click(reset_all_camera,inputs=ddWardrobe,            outputs=ddWardrobe)    
            resetAllButton.click(reset_all_camera,inputs=ddWardrobeSub,         outputs=ddWardrobeSub)    
            resetAllButton.click(reset_all_camera,inputs=ddFootwear,            outputs=ddFootwear)    
            resetAllButton.click(reset_all_camera,inputs=ddFootwearSub,         outputs=ddFootwearSub)              
            resetAllButton.click(reset_all_camera,inputs=ddFaceShape,           outputs=ddFaceShape)    
            resetAllButton.click(reset_all_camera,inputs=ddFaceExpression,      outputs=ddFaceExpression)    
            resetAllButton.click(reset_all_camera,inputs=ddHairColor,           outputs=ddHairColor)    
            resetAllButton.click(reset_all_camera,inputs=ddHairCut,             outputs=ddHairCut)    
            resetAllButton.click(reset_all_camera,inputs=ddEyeColor,            outputs=ddEyeColor)
            resetAllButton.click(reset_all_camera,inputs=ddEyeShape,            outputs=ddEyeShape) 
            resetAllButton.click(reset_all_camera,inputs=ddNose,                outputs=ddNose) 
            resetAllButton.click(reset_all_camera,inputs=ddLips,                outputs=ddLips)  
            resetAllButton.click(reset_all_camera,inputs=ddChin,                outputs=ddChin)             
            resetAllButton.click(reset_all_camera,inputs=ddHairAccessories,     outputs=ddHairAccessories)    
            resetAllButton.click(reset_all_camera,inputs=ddAnimalEars,          outputs=ddAnimalEars)
            resetAllButton.click(reset_all_camera,inputs=ddEarrings,            outputs=ddEarrings) 
            resetAllButton.click(reset_all_camera,inputs=ddNeckless,            outputs=ddNeckless) 
            resetAllButton.click(reset_all_camera,inputs=ddHat,                 outputs=ddHat) 
            resetAllButton.click(reset_all_camera,inputs=ddGlasses,             outputs=ddGlasses) 
            resetAllButton.click(reset_all_camera,inputs=ddQuickBackGround,     outputs=ddQuickBackGround)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleFullBodyArmor, outputs=ddFemaleFullBodyArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleHeadArmor,     outputs=ddFemaleHeadArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleNeckArmor,     outputs=ddFemaleNeckArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleShoulderArmor, outputs=ddFemaleShoulderArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleChestArmor,    outputs=ddFemaleChestArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleLegArmor,      outputs=ddFemaleLegArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleGroinArmor,    outputs=ddFemaleGroinArmor)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleWeapons,       outputs=ddFemaleWeapons)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleWeaponsSub,    outputs=ddFemaleWeaponsSub)
            resetAllButton.click(reset_all_camera,inputs=ddFemaleShield,        outputs=ddFemaleShield)
       
        # Male Character
        with gr.Tab("Male Character"):
         
        # General section
            with gr.Column(variant="panel"):
                with gr.Row(variant="panel"):
                    gr.HTML('<h1>General</h1>') 
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    resetAllButton = gr.Button('Reset ALL Male Character', variant = 'stop' , size = "sm")


            # Beauty Descriptor  / Content Rating  
                with gr.Row(variant="panel"):
                    ddMaleBeautyDescriptor = Dropdown_List_From_File(MaleBeautifiersDir,"Beauty Descriptor", True)
                    ddMaleContentRating    = Dropdown_List_From_File(MaleContentRatingDir,"Content Rating", True) 
                    slMaleContent          = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Male  type  / Submenu     
                with gr.Row(variant="panel"):
                    ddMaleType       = Dropdown_List_From_File(MaleTypeDir,"Male Type", True)
                    ddMaleSubType    = Dropdown_List_From_SubFile(MaleSubTypeDir,ddMaleType,"Submenu", True)
                    ddMaleType.change(RefreshDropDown5, ddMaleType, ddMaleSubType)
                    slMaleTypeStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
                       
            # Male god  / Submenu     
                with gr.Row(variant="panel"):
                    ddMaleGodType    = Dropdown_List_From_File(MaleGodTypeDir,"God", True)
                    ddMaleGod        = Dropdown_List_From_SubFile(MaleGodDir,ddMaleGodType,"Submenu", True)
                    ddMaleGodType.change(RefreshDropDown14, ddMaleGodType, ddMaleGod)
                    slMaleGodStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Male Embedding     
                with gr.Row(variant="panel"):
                    ddMaleEmbedding      = Dropdown_List_From_File(MaleEmbeddingsDir,"Embedding", True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slMaleEmbeddingStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Male Lora 
                with gr.Row(variant="panel"):
                    ddMaleLora         = Dropdown_List_From_File(MaleLoraDir,"Lora",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slMaleLoraStrenght  = gr.Slider(0,2, value=1.0,step=0.05,show_label=False)   


            # Origin-Nationality / Skin Color     
                with gr.Row(variant="panel"):
                    ddMaleOrigin    = Dropdown_List_From_File(MaleOriginOrNationalityDir,"Origin or Nationality", True)
                    ddMaleSkinColor = Dropdown_List_From_File(MaleSkinColorDir,"Skin Color", True)
                    slMaleOriginSkinStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
            

            # Body View / Camera Angle      
                with gr.Row(variant="panel"):
                    ddMaleBodyView    = Dropdown_List_From_File(MaleBodyViewDir,"Body View", True)
                    ddMaleBodyAngle   = Dropdown_List_From_File(MaleBodyAngleDir, "Body Angle", True)
                    slMaleBodyAngleStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)                    

            # Camera focus / Looking Where                         
                with gr.Row(variant="panel"):
                    ddMaleCameraFocus = Dropdown_List_From_File(MaleCameraFocusDir,"Camera Focus",True)
                    ddMaleLooking = Dropdown_List_From_File(MaleLookingWhereDir,"Looking Where",True)
                    slMaleFocusLooking = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

        # Body 
            with gr.Column(variant="panel"):
                gr.HTML('<h1>Body</h1>') 

            # Body Type    
                with gr.Row(variant="panel"):
                    ddMaleBodyType   = Dropdown_List_From_File(MaleBodyTypeDir,"Body Type", True)
                    ddMaleBodyHeight = Dropdown_List_From_File(MaleBodyHeightDir,"Body Height",True) 
                    slBodyHeightStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False) 

            # Age / Skin     
                with gr.Row(variant="panel"):
                    ddMaleAge     = Dropdown_List_From_File(MaleAgeDir,"Age", True)
                    ddMaleSkin    = Dropdown_List_From_File(MaleSkinDir,"Skin", True)
                    slMaleAgeSkinStrenght   = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Wardrobe
                with gr.Row(variant="panel"):
                    ddMaleWardrobe          = Dropdown_List_From_File(MaleWardrobeDir,"Wardrobe", True)
                    ddMaleWardrobeSub       = Dropdown_List_From_SubFile(MaleWardorbeSubDir,ddMaleWardrobe,"Submenu",True)
                    ddMaleWardrobe.change(RefreshDropDown6,ddMaleWardrobe,ddMaleWardrobeSub) 
                    slMaleWardrobeStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Footwear
                with gr.Row(variant="panel"):
                    ddMaleFootwear          = Dropdown_List_From_File(MaleFootwearDir,"Footwear", True)
                    ddMaleFootwearSub       = Dropdown_List_From_SubFile(MaleFootwearSubDir,ddMaleFootwear,"Submenu",True)
                    ddMaleFootwear.change(RefreshDropDown7,ddMaleFootwear,ddMaleFootwearSub) 
                    slMaleFootwearStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

        # Head section

            with gr.Column(variant="panel"):
                gr.HTML('<h1>Head</h1>') 
            # Face                                  
                with gr.Row(variant="panel"):       
                    ddMaleFaceShape      = Dropdown_List_From_File(MaleFaceShapeDir,"Face Shape", True)
                    ddMaleFaceExpression = Dropdown_List_From_File(MaleFaceExpressionDir,"Face Expression",True)
                    slMaleShapeExpressionStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Hair                          
                with gr.Row(variant="panel"):   
                    ddMaleHairColor = Dropdown_List_From_File(MaleHairColorDir,"Hair Color", True)
                    ddMaleHairCut   = Dropdown_List_From_File(MaleHairCutDir,"Haircuts",True)
                    slMaleColorCutStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)
         
            # Eyes                                 
                with gr.Row(variant="panel"):
                    ddMaleEyeColor = Dropdown_List_From_File(MaleEyeColorDir,"Eye Color", True)
                    ddMaleEyeShape = Dropdown_List_From_File(MaleEyeShapeDir,"Eye shape",True)
                    slMaleColorShapeStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # EyeBrows / Glasses                        
                with gr.Row(variant="panel"):
                    ddMaleEyeBrows = Dropdown_List_From_File(MaleEyeBrowsDir,"Eye Brows", True)
                    ddMaleGlasses  = Dropdown_List_From_File(MaleGlassesDir,"Glasses",True)
                    slMaleBrowsGlassesStrenght = gr.Slider(0 ,2, value=1.0, step=0.05, show_label=False)

            # Nose / Chin                                   
                with gr.Row(variant="panel"):
                    ddMaleNose = Dropdown_List_From_File(MaleNoseDir,"Nose",True)
                    ddMaleChin = Dropdown_List_From_File(MaleChinDir,"Chin",True)
                    slMaleNoseChinStrenght = gr.Slider(0 ,2, value=1.0, step=0.05, show_label=False)
            
        # Head Acessories

            # Mustache / Beard     
            with gr.Column(variant="panel"):
                with gr.Row():
                    ddMustache  = Dropdown_List_From_File(MaleMustacheDir,"Moustache", True)
                    ddBeard     = Dropdown_List_From_File(MaleBeardDir,"Beard", True)
                    slMustacheBeardStrenght = gr.Slider(0, 2, value=1.0, step=0.05,show_label=False)

            # Headwear  / Neckless     
                with gr.Row(variant="panel"):
                    ddMaleHeadWear       = Dropdown_List_From_File(MaleHeadWearDir,"Head wear", True)
                    ddMaleNeckless       = Dropdown_List_From_File(MaleNecklessDir,"Neckless", True)
                    slMaleNecklessStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Quick background 
                with gr.Row(variant="panel"):
                    ddMaleQuickBackGround = Dropdown_List_From_File(QuickBackGroundDir,"Quick Background",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slMaleBackGroundStrenght = gr.Slider(0,2,value=1.0,step=0.05,show_label=False) 


        # RPG  
            with gr.Column(variant="panel"):
                gr.HTML('<h1>RPG Dress up Corner</h1>') 

            # Full Body Armor 
                with gr.Row(variant="panel"):
                    ddMaleFullBodyArmor = Dropdown_List_From_File(MaleBodyArmorDir,"Full Body Armor",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slMaleFullBodyArmorStrenght = gr.Slider(0,2,value=1.0,step=0.05,show_label=False)

            # Head Protection  / Neck Protection     
                with gr.Row(variant="panel"):
                    ddMaleHeadArmor       = Dropdown_List_From_File(MaleHeadProtectionDir,"Head Protection", True)
                    ddMaleNeckArmor       = Dropdown_List_From_File(MaleNeckProtectionDir,"Neck Protection", True)
                    slMaleHeadNeckStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Shoulder Protection / Torso Protection
                with gr.Row(variant="panel"):
                    ddMaleShoulderArmor    = Dropdown_List_From_File(MaleShoulderProtectionDir,"Shoulder Protection", True)
                    ddMaleChestArmor       = Dropdown_List_From_File(MaleTorsoProtectionDir,"Torso Protection", True)
                    slMaleShoulderChestStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Legs Protection / Groin Protection
                with gr.Row(variant="panel"):
                    ddMaleLegArmor     = Dropdown_List_From_File(MaleLegProtectionDir,"Legs Protection ", True)
                    ddMaleGroinArmor   = Dropdown_List_From_File(MaleGroinProtectionDir,"Groin Protection", True)
                    slMaleLegGroinStrenght = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Weapons
                with gr.Row(variant="panel"):
                    ddMaleWeapons          = Dropdown_List_From_File(MaleWeaponDir,"Weapons", True)
                    ddMaleWeaponsSub       = Dropdown_List_From_SubFile(MaleWeaponSubmenuDir,ddMaleWeapons,"Submenu",True)
                    ddMaleWeapons.change(RefreshDropDown8,ddMaleWeapons,ddMaleWeaponsSub) 
                    slMaleWeaponsStrenght  = gr.Slider(0, 2, value=1.0, step=0.05, show_label=False)

            # Hand Held Shield
                with gr.Row(variant="panel"):
                    ddMaleShield = Dropdown_List_From_File(MaleShieldDir,"Hand held Shield",True)
                    gr.HTML('<h1 style="display: none;">a</h1>')
                    slMaleShield = gr.Slider(0,2,value=1.0,step=0.05,show_label=False)

            resetAllButton.click(reset_all_camera,inputs=ddMaleBeautyDescriptor,outputs=ddMaleBeautyDescriptor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleContentRating,outputs=ddMaleContentRating)
            resetAllButton.click(reset_all_camera,inputs=ddMaleType,outputs=ddMaleType)
            resetAllButton.click(reset_all_camera,inputs=ddMaleSubType,outputs=ddMaleSubType)
            resetAllButton.click(reset_all_camera,inputs=ddMaleEmbedding,outputs=ddMaleEmbedding)
            resetAllButton.click(reset_all_camera,inputs=ddMaleLora,outputs=ddMaleLora)
            resetAllButton.click(reset_all_camera,inputs=ddMaleOrigin,outputs=ddMaleOrigin)
            resetAllButton.click(reset_all_camera,inputs=ddMaleSkinColor,outputs=ddMaleSkinColor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleBodyView,outputs=ddMaleBodyView)
            resetAllButton.click(reset_all_camera,inputs=ddMaleBodyAngle,outputs=ddMaleBodyAngle)
            resetAllButton.click(reset_all_camera,inputs=ddMaleLooking,outputs=ddMaleLooking)
            resetAllButton.click(reset_all_camera,inputs=ddMaleCameraFocus,outputs=ddMaleCameraFocus)
            resetAllButton.click(reset_all_camera,inputs=ddMaleBodyType,outputs=ddMaleBodyType)
            resetAllButton.click(reset_all_camera,inputs=ddMaleAge,outputs=ddMaleAge)
            resetAllButton.click(reset_all_camera,inputs=ddMaleSkin,outputs=ddMaleSkin)
            resetAllButton.click(reset_all_camera,inputs=ddMaleBodyHeight,outputs=ddMaleBodyHeight)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleWardrobe,outputs=ddMaleWardrobe)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleWardrobeSub,outputs=ddMaleWardrobeSub)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleFootwear,outputs=ddMaleFootwear)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleFootwearSub,outputs=ddMaleFootwearSub)              
            resetAllButton.click(reset_all_camera,inputs=ddMaleFaceShape,outputs=ddMaleFaceShape)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleFaceExpression,outputs=ddMaleFaceExpression)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleHairColor,outputs=ddMaleHairColor)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleHairCut,outputs=ddMaleHairCut)    
            resetAllButton.click(reset_all_camera,inputs=ddMaleEyeColor,outputs=ddMaleEyeColor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleEyeShape,outputs=ddMaleEyeShape) 
            resetAllButton.click(reset_all_camera,inputs=ddMaleEyeBrows,outputs=ddMaleEyeBrows) 
            resetAllButton.click(reset_all_camera,inputs=ddMaleGlasses,outputs=ddMaleGlasses)  
            resetAllButton.click(reset_all_camera,inputs=ddMaleNose,outputs=ddMaleNose)
            resetAllButton.click(reset_all_camera,inputs=ddMaleChin,outputs=ddMaleChin)             
            resetAllButton.click(reset_all_camera,inputs=ddMaleHeadWear,outputs=ddMaleHeadWear)    
            resetAllButton.click(reset_all_camera,inputs=ddMustache,outputs=ddMustache)
            resetAllButton.click(reset_all_camera,inputs=ddBeard,outputs=ddBeard) 
            resetAllButton.click(reset_all_camera,inputs=ddMaleNeckless,outputs=ddMaleNeckless)  
            resetAllButton.click(reset_all_camera,inputs=ddMaleQuickBackGround,outputs=ddMaleQuickBackGround)
            resetAllButton.click(reset_all_camera,inputs=ddMaleFullBodyArmor,outputs=ddMaleFullBodyArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleHeadArmor,outputs=ddMaleHeadArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleNeckArmor,outputs=ddMaleNeckArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleShoulderArmor,outputs=ddMaleShoulderArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleChestArmor,outputs=ddMaleChestArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleLegArmor,outputs=ddMaleLegArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleGroinArmor,outputs=ddMaleGroinArmor)
            resetAllButton.click(reset_all_camera,inputs=ddMaleWeapons,outputs=ddMaleWeapons)
            resetAllButton.click(reset_all_camera,inputs=ddMaleWeaponsSub,outputs=ddMaleWeaponsSub)
            resetAllButton.click(reset_all_camera,inputs=ddMaleShield,outputs=ddMaleShield)
            resetAllButton.click(reset_all_camera,inputs=ddMaleGodType,outputs=ddMaleGodType)
            resetAllButton.click(reset_all_camera,inputs=ddMaleGod,outputs=ddMaleGod)

       ## Scene 
       #with gr.Tab("Scene"):
       #    # General section
       #    with gr.Column(variant="panel"):
       #        with gr.Row():
       #            lGeneral = gr.Label(value = "General",label= "", variant="Third Label", size ="sm", text_align="left", content_align="left" , info= "Poruka")
       #

       ## Objects 
       #with gr.Tab("Objects"):
       #    # General section
       #    with gr.Column(variant="panel"):
       #        with gr.Row():
       #            lGeneral = gr.Label(value = "General",label= "", variant="Third Label", size ="sm", text_align="left", content_align="left" , info= "Poruka")
       #

       ## Creatures
       #with gr.Tab("Creatures"):
       #    # General section
       #    with gr.Column(variant="panel"):
       #        with gr.Row():
       #            lGeneral = gr.Label(value = "General",label= "", variant="Third Label", size ="sm", text_align="left", content_align="left" , info= "Poruka")
        
        # Settings
        with gr.Tab("Settings"):

            with gr.Column(variant="panel"):
                gr.HTML('<br/>')
                gr.HTML('<h1>Settings</h1>')

                gr.HTML('<h2>Default Tab</h2>')
                gr.HTML('<p>Default Tab when u start the script')

                Tabs = []
                Tabs.append("Default")
                Tabs.append("General")
                Tabs.append("Female Character")
                Tabs.append("Male Charcter")
                Tabs.append("Settings")
       
                with gr.Row():
                    ddTab =  gr.Dropdown(Tabs, label="", value="General")

            # General section     
                gr.HTML('<h2>Seed Settings</h2>')
                with gr.Row():
                    cbChangeCount = gr.Checkbox(
                        value=True, label="Set batch count to prompt count")
                with gr.Row():
                    cbIncreaseSeed = gr.Checkbox(
                        value=False, label="Increase seed with batch size")
                    
                gr.HTML('<h2>Helper Tags</h2>')
                gr.HTML('<p>Reccomended to be ENABLED for best results.</p>')
                gr.HTML('<p>Some values from dropdowns will add aditional words to positive or/and negative prompts.</p>')
                gr.HTML('<p>Uncheck this only if you want to remove tags added by the script without your choice.</p>')
        
                with gr.Row():
                    cbPositives = gr.Checkbox(value = True, label = "Enable Positives")
                    cbNegatives = gr.Checkbox(value = True, label = "Enable Negatives")

                gr.HTML('<h2>Licence</h2>')
                gr.HTML('<p>Tool by Peaksel is a free software, released under General Public <a href="https://www.gnu.org/licenses/gpl-3.0.en.html" target="_blank" style="color: #3498db; text-decoration: underline;">License 3.0()</a>.<br/>'
                        + 'It follows the same license as the <a href="https://github.com/some9000/StylePile" target="_blank" style="color: #3498db; text-decoration: underline;">Style Pile</a> script, which was used as an inspiration and starting code base for this project.</p>')
                gr.HTML('<h2>Credits</h2>')
                gr.HTML('<p>Script developed and released by Peaksel, video games company from Serbia (website, LinkedIN): <br/>' \
                        + 'Marko Petkovic <a href="https://www.linkedin.com/in/petkovicmarko/" target="_blank" style="color: #3498db; text-decoration: underline;">LinkedIn</a> : UI, data collection and end user testing  <br/>' \
                        + 'Dusan Ilic <a href="https://www.linkedin.com/in/du%C5%A1an-ili%C4%87-a9a85173/" target="_blank" style="color: #3498db;; text-decoration: underline;">LinkedIn</a> : development and functional testing  <br/>'
                        + 'Andrija Ivkovic <a href="https://www.linkedin.com/in/andrija-ivkovic-6a6285261/" target="_blank" style="color: #3498db; text-decoration: underline;">LinkedIn</a> : development, data collection and functional testing  <br/>' \
                        + 'Values for the script are obtained from multiple sources:<a href="https://danbooru.donmai.us/" target="_blank" style="color: #3498db; text-decoration: underline;">Danbooru</a>, AI chatbots (<a href="https://chat.openai.com/" target="_blank" style="color: #3498db; text-decoration: underline;">ChatGPT</a>, <a href="https://bard.google.com/" target="_blank" style="color: #3498db; text-decoration: underline;">Bard</a>, <a href="https://www.bing.com/search?q=bing+ai&form=ANNTH1&refig=2422a3eae03b42f5a8961a9afb6f42d8" target="_blank" style="color: #3498db; text-decoration: underline;">Bing</a>) and <a href="https://civitai.com/?query=wildcards&view=feed" target="_blank" style="color: #3498db; text-decoration: underline;"> Civitai </a> community</p>')

        return [
            ddTab,
            cbChangeCount,
            cbIncreaseSeed,
            strSequentialPrompt,
            strSubSequentialPrompt,
            strRandomPromptA,
            strRandomPromptB,
            strRandomPromptC,
            resetButton,
            #editButton,
            ddBeautifiers,
            ddDetails,
            ddStyleLora,
            slStyleLoraStrength,
            ddMediumType,
            ddMediumSubType,
            slMediumStrength,
            #ddStyleEMB,
            ddStyleEmbedding,
            slStyleEmbeddingStrength,
            ddStyleGeneral,
            ddStyleGame,
            slStyleGameStrength,
            slStyleGeneralStrength,
            ddNegatives,
            #ckbutton1,
            ckbutton2,
            ckbutton3,
            ckbutton4,
            ckbutton5,
            ckbutton6,
            ckbutton7,
            ckbutton8,
            ckbutton9,
            ckbutton10,
            ckbutton11,
            ckbutton12,
            ckbutton13,
            ckbutton14,
            ckbutton15,
            ckbutton16,
            ckbutton17,
            ckbutton18,
            ckbutton19,
            ckbutton20,
            ckbutton21,
            ckbutton22,
            ckbutton23,
            ckbutton24,
            ddMaterial,
            ddMaterialSub,
            slMaterialStrength,
            ddSeason,
            ddHoliday,
            slSeasonHolidayStrength,
            ddLighting,
            ddLightingSub,
            slLightingStrength,
            ddLightingEffect,
            slLightingEffectStrength,
            ddColorTone,
            ddColorScheme,
            slResultColorStrength,
            slBeautifierStrength,
            ddCameraShotType,
            ddCameraShotAngle,
            ddCameraBrand,
            ddCameraFilmSize,
            ddCameraFocus,
            ddCameraFocalLength,
            ddPhotographers,
            ddPhotographyType,
            slPhotographyStrenght,
            slCameraGroup1,
            slCameraGroup2,
            slCameraGroup3,
            ddArtistSingle,
            ddArtistSimilar,
            slArtistGroupStrength,
            cbPositives,
            cbNegatives,
            ddContentRating,
            ddBeautyDescriptor,
            slBeautyStrenght,
            ddFemaleType,
            ddSpecificPerson,
            ddGoddessType,
            ddGoddess,
            slGoddessStrenght,
            slFemaleTypeStrenght,
            slCelebrityEmbedding,
            slOriginColorStrenght,
            ddEmbedding,
            ddLora,
            slLoraStrenght,
            ddAge,
            ddSkin,
            slAgeSkinStrenght,
            ddOriginOrNationality,
            ddSkinColor,
            ddBodyView,
            ddCameraAngle,
            ddHairColor,
            ddHairCut,
            slColorCutStrenght,
            ddEyeColor,
            ddEyeShape, 
            slColorShapeStrenght,  
            ddFaceShape,
            ddFaceExpression,
            slShapeExpressionStrenght,
            ddEyeBrows,
            ddNose,
            slBrowsNoseStrenght,
            ddLips,
            ddChin,
            slLipsChinStrenght,
            ddCameraFFocus,
            ddLookingWhere,
            slBodyAngleStrenght,
            slCameraLookingWhereStrenght,
            ddHairAccessories,
            ddAnimalEars,
            slHairEarsStrenght,
            ddEarrings,
            ddNeckless,
            slEarringsNecklessStrenght,
            ddHat,
            ddGlasses,
            slHatGlassesStrenght,
            ddQuickBackGround,
            slBackGroundStrenght,
            ddBodyType,
            slBodyTypeStrenght,
            ddBreastSize,
            ddBreastDesc,
            slBreastStrenght,
            ddAssSize,
            ddAssDesc,
            slAssStrenght,
            ddHips,
            ddLegsDesc,
            slHipsLegsStrenght,
            ddWardrobe,
            ddWardrobeSub,
            slWardrobeStrenght,
            ddFootwear,
            ddFootwearSub,
            slFootwearStrenght,
            ddMaleBeautyDescriptor,
            ddMaleContentRating,
            slMaleContent,
            ddMaleType,
            ddMaleSubType,
            ddMaleGodType,
            ddMaleGod,
            slMaleGodStrenght,
            slMaleTypeStrenght,
            ddMaleEmbedding,
            slMaleEmbeddingStrenght,
            ddMaleLora,
            slMaleLoraStrenght,
            ddMaleOrigin,
            ddMaleSkinColor,
            slMaleOriginSkinStrenght,
            ddMaleBodyView,
            ddMaleBodyAngle,
            slMaleBodyAngleStrenght,
            ddMaleCameraFocus,
            ddMaleLooking,
            slMaleFocusLooking,
            ddMaleBodyType,
            ddMaleBodyHeight,
            slBodyHeightStrenght,
            ddMaleAge,
            ddMaleSkin,
            slMaleAgeSkinStrenght,
            ddMaleWardrobe,
            ddMaleWardrobeSub,
            slMaleWardrobeStrenght,
            ddMaleFootwear,
            ddMaleFootwearSub,
            slMaleFootwearStrenght,
            ddMaleFaceShape,
            ddMaleFaceExpression,
            slMaleShapeExpressionStrenght,
            ddMaleHairColor,
            ddMaleHairCut,
            slMaleColorCutStrenght,
            ddMaleEyeColor,
            ddMaleEyeShape,
            slMaleColorShapeStrenght,
            ddMaleEyeBrows,
            ddMaleGlasses,
            slMaleBrowsGlassesStrenght,
            ddMaleNose,
            ddMaleChin,
            slMaleNoseChinStrenght,
            ddMustache,
            ddBeard,
            slMustacheBeardStrenght,
            ddMaleHeadWear,
            ddMaleNeckless,
            slMaleNecklessStrenght,
            ddMaleQuickBackGround,
            slMaleBackGroundStrenght,
            ddMaleFullBodyArmor,
            slMaleFullBodyArmorStrenght,
            ddMaleHeadArmor,
            ddMaleNeckArmor,
            slMaleHeadNeckStrenght,
            ddMaleShoulderArmor,
            ddMaleChestArmor,
            slMaleShoulderChestStrenght,
            ddMaleLegArmor,
            ddMaleGroinArmor,
            slMaleLegGroinStrenght,
            ddMaleWeapons,
            ddMaleWeaponsSub,
            slMaleWeaponsStrenght,
            ddMaleShield,
            slMaleShield,
            ddFemaleFullBodyArmor,
            slFemaleFullBodyArmorStrenght,
            ddFemaleHeadArmor,
            ddFemaleNeckArmor,
            slFemaleHeadNeckStrenght,
            ddFemaleShoulderArmor,
            ddFemaleChestArmor,
            slFemaleShoulderChestStrenght,
            ddFemaleLegArmor,
            ddFemaleGroinArmor,
            slFemaleLegGroinStrenght,
            ddFemaleWeapons,
            ddFemaleWeaponsSub,
            slFemaleWeaponsStrenght,
            ddFemaleShield,
            slFemaleShield
                ]

    # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

    def run(self, p,
            ddTab,
            cbChangeCount,
            cbIncreaseSeed,
            strSequentialPrompt: str,
            strSubSequentialPrompt: str,
            strRandomPromptA: str,
            strRandomPromptB: str,
            strRandomPromptC: str,
            resetButton,
            #editButton,
            ddBeautifiers,
            ddDetails,
            ddStyleLora,
            slStyleLoraStrength,
            ddMediumType,
            ddMediumSubType,
            slMediumStrength,
            #ddStyleEMB,
            ddStyleEmbedding,
            slStyleEmbeddingStrength,
            ddStyleGeneral,
            ddStyleGame,
            slStyleGameStrength,
            slStyleGeneralStrength,
            ddNegatives,
            #ckbutton1,
            ckbutton2,
            ckbutton3,
            ckbutton4,
            ckbutton5,
            ckbutton6,
            ckbutton7,
            ckbutton8,
            ckbutton9,
            ckbutton10,
            ckbutton11,
            ckbutton12,
            ckbutton13,
            ckbutton14,
            ckbutton15,
            ckbutton16,
            ckbutton17,
            ckbutton18,
            ckbutton19,
            ckbutton20,
            ckbutton21,
            ckbutton22,
            ckbutton23,
            ckbutton24,
            ddMaterial,
            ddMaterialSub,
            slMaterialStrength,
            ddSeason,
            ddHoliday,
            slSeasonHolidayStrength,
            ddLighting,
            ddLightingSub,
            slLightingStrength,
            ddLightingEffect,
            slLightingEffectStrength,
            ddColorTone,
            ddColorScheme,
            slResultColorStrength,
            slBeautifierStrength,
            ddCameraShotType,
            ddCameraShotAngle,
            ddCameraBrand,
            ddCameraFilmSize,
            ddCameraFocus,
            ddCameraFocalLength,
            ddPhotographers,
            ddPhotographyType,
            slPhotographyStrenght,
            slCameraGroup1,
            slCameraGroup2,
            slCameraGroup3,
            ddArtistSingle,
            ddArtistSimilar,
            slArtistGroupStrength,
            cbPositives,
            cbNegatives,
            ddContentRating,
            ddBeautyDescriptor,
            slBeautyStrenght,
            ddFemaleType,
            ddSpecificPerson,
            ddGoddessType,
            ddGoddess,
            slGoddessStrenght,
            slFemaleTypeStrenght,
            slCelebrityEmbedding,
            slOriginColorStrenght,
            ddEmbedding,
            ddLora,
            slLoraStrenght,
            ddAge,
            ddSkin,
            slAgeSkinStrenght,
            ddOriginOrNationality,
            ddSkinColor,
            ddBodyView,
            ddCameraAngle,
            ddHairColor,
            ddHairCut,
            slColorCutStrenght,
            ddEyeColor,
            ddEyeShape, 
            slColorShapeStrenght,  
            ddFaceShape,
            ddFaceExpression,
            slShapeExpressionStrenght,
            ddEyeBrows,
            ddNose,
            slBrowsNoseStrenght,
            ddLips,
            ddChin,
            slLipsChinStrenght,
            ddCameraFFocus,
            ddLookingWhere,
            slBodyAngleStrenght,
            slCameraLookingWhereStrenght,
            ddHairAccessories,
            ddAnimalEars,
            slHairEarsStrenght,
            ddEarrings,
            ddNeckless,
            slEarringsNecklessStrenght,
            ddHat,
            ddGlasses,
            slHatGlassesStrenght,
            ddQuickBackGround,
            slBackGroundStrenght,
            ddBodyType,
            slBodyTypeStrenght,
            ddBreastSize,
            ddBreastDesc,
            slBreastStrenght,
            ddAssSize,
            ddAssDesc,
            slAssStrenght,
            ddHips,
            ddLegsDesc,
            slHipsLegsStrenght,
            ddWardrobe,
            ddWardrobeSub,
            slWardrobeStrenght,
            ddFootwear,
            ddFootwearSub,
            slFootwearStrenght,
            ddMaleBeautyDescriptor,
            ddMaleContentRating,
            slMaleContent,
            ddMaleType,
            ddMaleSubType,
            ddMaleGodType,
            ddMaleGod,
            slMaleGodStrenght,
            slMaleTypeStrenght,
            ddMaleEmbedding,
            slMaleEmbeddingStrenght,
            ddMaleLora,
            slMaleLoraStrenght,
            ddMaleOrigin,
            ddMaleSkinColor,
            slMaleOriginSkinStrenght,
            ddMaleBodyView,
            ddMaleBodyAngle,
            slMaleBodyAngleStrenght,
            ddMaleCameraFocus,
            ddMaleLooking,
            slMaleFocusLooking,
            ddMaleBodyType,
            ddMaleBodyHeight,
            slBodyHeightStrenght,
            ddMaleAge,
            ddMaleSkin,
            slMaleAgeSkinStrenght,
            ddMaleWardrobe,
            ddMaleWardrobeSub,
            slMaleWardrobeStrenght,
            ddMaleFootwear,
            ddMaleFootwearSub,
            slMaleFootwearStrenght,
            ddMaleFaceShape,
            ddMaleFaceExpression,
            slMaleShapeExpressionStrenght,
            ddMaleHairColor,
            ddMaleHairCut,
            slMaleColorCutStrenght,
            ddMaleEyeColor,
            ddMaleEyeShape,
            slMaleColorShapeStrenght,
            ddMaleEyeBrows,
            ddMaleGlasses,
            slMaleBrowsGlassesStrenght,
            ddMaleNose,
            ddMaleChin,
            slMaleNoseChinStrenght,
            ddMustache,
            ddBeard,
            slMustacheBeardStrenght,
            ddMaleHeadWear,
            ddMaleNeckless,
            slMaleNecklessStrenght,
            ddMaleQuickBackGround,
            slMaleBackGroundStrenght,
            ddMaleFullBodyArmor,
            slMaleFullBodyArmorStrenght,
            ddMaleHeadArmor,
            ddMaleNeckArmor,
            slMaleHeadNeckStrenght,
            ddMaleShoulderArmor,
            ddMaleChestArmor,
            slMaleShoulderChestStrenght,
            ddMaleLegArmor,
            ddMaleGroinArmor,
            slMaleLegGroinStrenght,
            ddMaleWeapons,
            ddMaleWeaponsSub,
            slMaleWeaponsStrenght,
            ddMaleShield,
            slMaleShield,
            ddFemaleFullBodyArmor,
            slFemaleFullBodyArmorStrenght,
            ddFemaleHeadArmor,
            ddFemaleNeckArmor,
            slFemaleHeadNeckStrenght,
            ddFemaleShoulderArmor,
            ddFemaleChestArmor,
            slFemaleShoulderChestStrenght,
            ddFemaleLegArmor,
            ddFemaleGroinArmor,
            slFemaleLegGroinStrenght,
            ddFemaleWeapons,
            ddFemaleWeaponsSub,
            slFemaleWeaponsStrenght,
            ddFemaleShield,
            slFemaleShield
            ):


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

            for y in range(SubIterationCount):

            # Variable initialization 
            # First Tab 
                # Clear the variables so random selection can work
                ColorTone = ""
                ColorTonePositives = ""
                ColorToneNegatives = ""
                ColorToneResult = ""
                ColorScheme = ""
                ColorSchemePositives = ""
                ColorSchemeNegatives = ""
                FinalResultColor = ""

                Beautifiers = ""
                BeautifiersPositives = ""
                BeautifiersNegatives = ""
                BeautifiersResult = ""
                Details = ""
                DetailsPositives = ""
                DetailsNegatives = ""
                BeautifiersDetailsFinal = ""

                # Preset the selection variables
                MainType = ""

                Medium = ""
                MediumPositives = ""
                MediumNegatives = ""
                MediumResult = ""
                MediumSub = ""
                MediumSubPositives = ""
                MediumSubNegatives = ""
                MediumFinal = ""

                NegativeTags = ""
                NegativeTagsFinal = ""

                NegativeEmbeddings = ""

                StyleLora = ""
                StyleLoraPositives = ""
                StyleLoraNegatives = ""
                StyleLoraResult = ""

                StyleEmbedding = ""
                StyleEmbeddingPositives = ""
                StyleEmbeddingNegatives = ""
                StyleEmbeddingResult = ""

                StyleGeneral = ""
                StyleGeneralPositives = ""
                StyleGeneralNegatives = ""
                StyleGeneralResult = ""
                StyleGame = ""
                StyleGamePositives = ""
                StyleGameNegatives = ""
                StyleFinal = ""

                Season = ""
                SeasonPositives = ""
                SeasonNegatives = ""
                SeasonResult = ""
                Holiday = ""
                HolidayPositives = ""
                HolidayNegatives = ""
                SeasonHolidayFinal = ""

                Material = ""
                MaterialPositives = ""
                MaterialNegatives = ""
                MaterialResult = ""
                MaterialSub = ""
                MaterialSubPositives = ""
                MaterialSubNegatives = ""
                MaterialFinal = ""

                Lighting = ""
                LightingPositives = ""
                LightingNegatives = ""
                LightingResult = ""
                LightingSub = ""
                LightingSubPositives = ""
                LightingSubNegatives = ""
                LightingFinal = ""

                LightingEffect = ""
                LightingEffectPositives = ""
                LightingEffectNegatives = ""
                LightingEffectResult = ""

                ShotType = ""
                CameraShotTypePositives = ""
                CameraShotTypeNegatives = ""
                ShotTypeResult = ""
                ShotAngle = ""
                CameraShotAnglePositives = ""
                CameraShotAngleNegatives = ""
                CameraResult1 = ""

                ShotBrand = ""
                CameraBrandPositives = ""
                CameraBrandNegatives = ""
                ShotBrandResult = ""
                ShotSize = ""
                CameraFilmSizePositives = ""
                CameraFilmSizeNegatives = ""
                CameraResult2 = ""

                ShotFocus = ""
                CameraFocusPositives = ""
                CameraFocusNegatives = ""
                ShotFocusResult = ""
                ShotFocalLen = ""
                CameraFocalLenPositives = ""
                CameraFocalLenNegatives = ""
                CameraResult3 = ""

                PhotographyType = ""
                PhotographyTypePositives = ""
                PhotographyTypeNegatives = ""
                PhotographyTypeResult = ""
                Photographers = ""
                PhotographersPositives = ""
                PhotographersNegatives = ""
                PhotographyFinal = ""

                SingleArtist = ""
                SingleArtistPositives = ""
                SingleArtistNegatives = ""
                SingleArtistResult = ""
                ArtistTheme = ""
                ArtistThemePositives = ""
                ArtistThemeNegatives = ""
                ArtistsFinal = ""

            # Seccond Tab

                # General Section
                BeautyDescriptor = ""
                BeautyDescriptorPositives = ""
                BeautyDescriptorNegatives = ""
                BeautyDescResult = ""
                ContentRating = ""
                ContentRatingPositives = ""
                ContentRatingNegatives = ""
                ContentRatingResult = ""
                 
                Age = ""
                AgeResult = ""
                AgePositives = ""
                AgeNegatives = ""
                Skin = ""
                SkinPositives = ""
                SkinNegatives = ""
                SkinResult = ""

                FemaleType = ""
                FemaleTypePositives = ""
                FemaleTypeNegatives = ""
                FemaleTypeResult = ""
                SpecificPerson = ""
                SpecificPersonPositives = ""
                SpecificPersonNegatives = ""
                FemaleTypeFinal = ""


                GoddessType = ""
                GoddessTypePositives = ""
                GoddessTypeNegatives = ""
                GoddessTypeResult = "" 
                Goddess = ""
                GoddessPositives = ""
                GoddessNegatives = ""
                GoddessFinal = ""

       
                Embedding = ""
                EmbeddingPositives = ""
                EmbeddingNegatives = ""
                CelebrityEmbeddingFinal = ""

                Lora = ""
                LoraPositives = ""
                LoraNegatives = ""
                LoraResult = ""

                OriginOrNationality = ""
                OriginOrNationalityPositives = ""
                OriginOrNationalityNegatives = ""
                OriginOrNationalityResult = ""
                SkinColor = ""
                SkinColorPositives = ""
                SkinColorNegatives = ""
                OriginColorFinal = ""

                BodyView = ""
                BodyViewPositives = ""
                BodyViewNegatives = ""
                BodyViewResult = ""
                CameraAngle = ""
                CameraAnglePositives = ""
                CameraAngleNegatives = ""
                BodyAngleFinal = ""

                CameraFocus = ""
                CameraFocusPositives = ""
                CameraFocusNegatives = ""
                CameraLookingFinal = ""
                LookingWhere = ""
                LookingWherePositives = ""
                LookingWhereNegatives = ""
                LookingWhereResult = ""

                # Head Section 
                HairColor = ""
                HairColorPositives = ""
                HairColorNegatives = ""
                ColorResult = ""
                HairCut = ""
                HairCutPositives = ""
                HairCutNegatives = ""
                ColorCutFinal = ""

                EyeColor = ""
                EyeColorPositives = ""
                EyeColorNegatives = ""
                EyeResult = ""
                EyeShape = ""
                EyeShapePositives = ""
                EyeShapeNegatives = ""
                EyeFinal = ""

                FaceShape = ""
                FaceShapePositives = ""
                FaceShapeNegatives = ""
                ShapeResult = ""
                FaceExpression = ""
                FaceExpressionPositives = ""
                FaceExpressionNegatives = ""
                ShapeExpressionFinal = ""

                EyeBrows = ""
                EyeBrowsPositives = ""
                EyeBrowsNegatives = ""
                BrowsResult = ""
                Nose = ""
                NosePositives = ""
                NoseNegatives = ""
                BrowsNoseFinal = ""

                Lips = ""
                LipPositives = ""
                LipNegatives = ""
                LipResult = ""
                Chin = ""
                ChinPositives = ""
                ChinNegatives = ""
                LipChinFinal = ""

                #Head Accessories 
                HairAccessory = ""
                HairAccessoryPositives = ""
                HairAccessoryNegatives = ""
                HairAccessoryResult = ""
                AnimalEars = ""
                AnimalEarsPositives = ""
                AnimalEarsNegatives = ""
                HairEarsFinal = ""

                Earrings = ""
                EarringsPositives = ""
                EarringsNegatives = ""
                EarringsResult = ""
                Neckless = ""
                NecklessPositives = ""
                NecklessNegatives = ""
                EarringsNecklessFinal = ""

                Hat = ""
                HatPositives = ""
                HatNegatives = ""
                HatResult = ""
                Glasses = ""
                GlassesPositives = ""
                GlassesNegatives = ""
                HatGlassesFinal = ""

                QuickBackGround = ""
                QuickBackGroundPositives = ""
                QuickBackGroundNegatives = ""
                QuickBackGroundResult = ""

            # Body
                # Body Type
                BodyType = ""
                BodyTypePositives = ""
                BodyTypeNegatives = ""
                BodyTypeFinal = ""

                # Breast Size / Desc
                BreastSize = ""
                BreastSizePositives = ""
                BreastSizeNegatives = ""
                BreastSizeResult = ""
                BreastDescriptor = ""
                BreastDescriptorPositives = ""
                BreastDescriptorNegatives = ""
                BreastFinal = ""

                # Ass size / Desc
                AssSize = ""
                AssSizePositives = ""
                AssSizeNegatives = ""
                AssSizeResult = ""
                AssDescriptor = ""
                AssDescriptorPositives = ""
                AssDescriptorNegatives = ""
                AssFinal = ""

                # Hips / legs 
                Hips = ""
                HipsPositives = ""
                HipsNegatives = ""
                HipsResult = ""
                LegsDescriptor = ""
                LegsDescriptorPositives = ""
                LegsDescriptorNegatives = ""
                HipsLegsFinal = ""

                # Wardrobe 
                Wardrobe = ""
                WardrobePositives = ""
                WardrobeNegatives = ""
                WardrobeResult = ""
                WardrobeSub = ""
                WardrobeSubPositives = ""
                WardrobeSubNegatives = ""
                WardrobeFinal = ""

                # Footwear
                Footwear = ""
                FootwearPositives = ""
                FootwearNegatives = ""
                FootwearResult = ""
                FootwearSub = ""
                FootwearSubPositives = ""
                FootwearSubNegatives = ""
                FootwearFinal = ""

                #RPG
                FemaleBodyArmor = ""
                FemaleBodyArmorPositives = ""
                FemaleBodyArmorNegatives = ""
                FemaleBodyArmorResult = ""

                FemaleHeadArmor = ""
                FemaleHeadArmorPositives = ""
                FemaleHeadArmorNegatives = ""
                FemaleHeadArmorResult = ""
                FemaleNeckArmor = ""
                FemaleNeckArmorPositives = ""
                FemaleNeckArmorNegatives = ""
                FemaleHeadNeckFinal = ""

                FemaleShoulderArmor = ""
                FemaleShoulderArmorPositives = ""
                FemaleShoulderArmorNegatives = ""
                FemaleShoulderArmorResult = ""
                FemaleChestArmor = ""
                FemaleChestArmorPositives = ""
                FemaleChestArmorNegatives = ""
                FemaleShoulderChestFinal = ""

                FemaleLegArmor = ""
                FemaleLegArmorPositives = ""
                FemaleLegArmorNegatives = ""
                FemaleLegArmorResult = ""
                FemaleGroinArmor = ""
                FemaleGroinArmorPositives = ""
                FemaleGroinArmorNegatives = ""
                FemaleLegGroinFinal = ""

                FemaleWeapon = ""
                FemaleWeaponPositives = ""
                FemaleWeaponNegatives = ""
                FemaleWeaponResult = ""
                FemaleWeaponSub = ""
                FemaleWeaponSubPositives = ""
                FemaleWeaponSubNegatives = ""
                FemaleWeaponsFinal = ""

                FemaleShield = ""
                FemaleShieldPositives = ""
                FemaleShieldNegatives = ""
                FemaleShieldFinal = ""

            # Male Character 
                MaleContentRating = ""
                MaleContentRatingPositives = ""
                MaleContentRatingNegatives = ""
                MaleContentRatingResult = ""
                MaleBeautyDescriptor = ""
                MaleBeautyDescriptorPositives = ""
                MaleBeautyDescriptorNegatives = ""
                MaleRatingDescFinal = ""

                MaleType = ""
                MaleTypePositives = ""
                MaleTypeNegatives = ""
                MaleTypeResult = ""
                MaleSubType = ""
                MaleSubTypePositives = ""
                MaleSubTypeNegatives = ""
                MaleTypeFinal = ""


                MaleGodType = ""
                MaleGodTypePositives = ""
                MaleGodTypeNegatives = ""
                MaleGodTypeResult = "" 
                MaleGod = ""
                MaleGodPositives = ""
                MaleGodNegatives = ""
                MaleGodFinal = ""

                MaleEmbedding = ""
                MaleEmbeddingPositives = ""
                MaleEmbeddingNegatives = ""
                MaleEmbeddingResult = ""

                MaleLora = ""
                MaleLoraPositives = ""
                MaleLoraNegatives = ""
                MaleLoraResult = ""

                MaleOriginOrNationality = ""
                MaleOriginOrNationalityPositives = ""
                MaleOriginOrNationalityNegatives = ""
                MaleOriginOrNationalityResult = ""
                MaleSkinColor = ""
                MaleSkinColorPositives = ""
                MaleSkinColorNegatives = ""
                MaleOriginColorFinal = ""

                MaleBodyView = ""
                MaleBodyViewPositives = ""
                MaleBodyViewNegatives = ""
                MaleBodyViewResult = ""
                MaleBodyAngle = ""
                MaleBodyAnglePositives = ""
                MaleBodyAngleNegatives = ""
                MaleViewAngleFinal = ""

                MaleLookingWhere = ""
                MaleLookingWherePositives = ""
                MaleLookingWhereNegatives = ""
                MaleLookingWhereResult = ""
                MaleBodyFocus = ""
                MaleBodyFocusPositives = ""
                MaleBodyFocusNegatives = ""
                MaleLookingFocusFinal = ""

            # Body
                MaleBodyType = ""
                MaleBodyTypePositives = ""
                MaleBodyTypeNegatives = ""
                MaleBodyTypeResult = ""
                MaleBodyHeight = ""
                MaleBodyHeightPositives = ""
                MaleBodyHeightNegatives = ""
                MaleTypeHeightFinal = ""

                MaleAge = ""
                MaleAgePositives = ""
                MaleAgeNegatives = ""
                MaleAgeResult = ""
                MaleSkin = ""
                MaleSkinPositives = ""
                MaleSkinNegatives = ""
                MaleAgeSkinFinal = ""

                MaleWardrobe = ""
                MaleWardrobePositives = ""
                MaleWardrobeNegatives = ""
                MaleWardrobeResult = ""
                MaleWardrobeSub = ""
                MaleWardrobeSubPositives = ""
                MaleWardrobeSubNegatives = ""
                MaleWardrobeFinal = ""

                MaleFootwear = ""
                MaleFootwearPositives = ""
                MaleFootwearNegatives = ""
                MaleFootwearResult = ""
                MaleFootwearSub = ""
                MaleFootwearSubPositives = ""
                MaleFootwearSubNegatives = ""
                MaleFootwearFinal = ""

                MaleFaceShape = ""
                MaleFaceShapePositives = ""
                MaleFaceShapeNegatives = ""
                MaleFaceShapeResult = ""
                MaleFaceExpression = ""
                MaleFaceExpressionPositives = ""
                MaleFaceExpressionNegatives = ""
                MaleShapeExpressionFinal = ""

                MaleHairColor = ""
                MaleHairColorPositives = ""
                MaleHairColorNegatives = ""
                MaleHairColorResult = ""
                MaleHairCut = ""
                MaleHairCutPositives = ""
                MaleHairCutNegatives = ""
                MaleHairFinal = ""

                MaleEyeColor = ""
                MaleEyeColorPositives = ""
                MaleEyeColorNegatives = ""
                MaleEyeColorResult = ""
                MaleEyeShape = ""
                MaleEyeShapePositives = ""
                MaleEyeShapeNegatives = ""
                MaleEyesFinal = ""

                MaleEyeBrows = ""
                MaleEyeBrowsPositives = ""
                MaleEyeBrowsNegatives = ""
                MaleEyeBrowsResult = ""
                MaleGlasses = ""
                MaleGlassesPositives = ""
                MaleGlassesNegatives = ""
                MaleBrowsGlassesFinal = ""

                MaleNose = ""
                MaleNosePositives = ""
                MaleNoseNegatives = ""
                MaleNoseResult = ""
                MaleChin = ""
                MaleChinPositives = ""
                MaleChinNegatives = ""
                MaleNoseChinFinal = ""

                MaleMustache = ""
                MaleMustachePositives = ""
                MaleMustacheNegatives = ""
                MaleMustacheResult = ""
                MaleBeard = ""
                MaleBeardPositives = ""
                MaleBeardNegatives = ""
                MaleMustacheBeardFinal = ""

                MaleHeadWear = ""
                MaleHeadWearPositives = ""
                MaleHeadWearNegatives = ""
                MaleHeadWearResult = ""
                MaleNeckless = ""
                MaleNecklessPositives = ""
                MaleNecklessNegatives = ""
                MaleHeadWearFinal = ""

                MaleQuickBackGround = ""
                MaleQuickBackGroundPositives = ""
                MaleQuickBackGroundNegatives = ""
                MaleQuickBackGroundResult = ""

                #RPG
                MaleBodyArmor = ""
                MaleBodyArmorPositives = ""
                MaleBodyArmorNegatives = ""
                MaleBodyArmorResult = ""

                MaleHeadArmor = ""
                MaleHeadArmorPositives = ""
                MaleHeadArmorNegatives = ""
                MaleHeadArmorResult = ""
                MaleNeckArmor = ""
                MaleNeckArmorPositives = ""
                MaleNeckArmorNegatives = ""
                MaleHeadNeckFinal = ""

                MaleShoulderArmor = ""
                MaleShoulderArmorPositives = ""
                MaleShoulderArmorNegatives = ""
                MaleShoulderArmorResult = ""
                MaleChestArmor = ""
                MaleChestArmorPositives = ""
                MaleChestArmorNegatives = ""
                MaleShoulderChestFinal = ""

                MaleLegArmor = ""
                MaleLegArmorPositives = ""
                MaleLegArmorNegatives = ""
                MaleLegArmorResult = ""
                MaleGroinArmor = ""
                MaleGroinArmorPositives = ""
                MaleGroinArmorNegatives = ""
                MaleLegGroinFinal = ""

                MaleWeapon = ""
                MaleWeaponPositives = ""
                MaleWeaponNegatives = ""
                MaleWeaponResult = ""
                MaleWeaponSub = ""
                MaleWeaponSubPositives = ""
                MaleWeaponSubNegatives = ""
                MaleWeaponsFinal = ""

                MaleShield = ""
                MaleShieldPositives = ""
                MaleShieldNegatives = ""
                MaleShieldFinal = ""

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
                # General 
 
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                result = Combine_Field_With_Slider(ddDetails,slBeautifierStrength,Details,DetailsDir,DetailsPositives,DetailsNegatives,BeautifiersDetailsFinal)

                Details,DetailsPositives,DetailsNegatives,BeautifiersDetailsFinal,slBeautifierStrength = result 

                result = Combine_Field_With_Slider(ddBeautifiers,slBeautifierStrength,Beautifiers,BeautifiersDir,BeautifiersPositives,BeautifiersNegatives,BeautifiersResult)

                Beautifiers,BeautifiersPositives,BeautifiersNegatives,BeautifiersResult,slBeautifierStrength = result


                # Mediums && SubType
                result = Combine_SubFields_With_Slider(ddMediumType,ddMediumSubType,slMediumStrength,MediumPositives,MediumNegatives,MediumSubPositives,MediumSubNegatives,Medium,MediumSub,MediumResult,MediumFinal,MediumsDir,MediumsSubDir)

                Medium,MediumSub,MediumPositives,MediumNegatives,MediumSubPositives,MediumSubNegatives,MediumResult,MediumFinal,slMediumStrength = result

                
                # Negatives 
                # Read the list of negative embeddings from a file and concat if needed
                if ddNegatives != "Not set":
                    if ddNegatives == "Random":
                        NegativeTags = random.choice(RandomFromFile(NegativesDir,False)) 
                    else :  
                        NegativeTags = ddNegatives.replace("*","")
                    if (NegativeTags == "general"):
                        NegativeTagsFinal = RandomFromFile(NegativesGeneralDir,False)
                    elif(NegativeTags == "general+B&W"):
                        NegativeTagsFinal = RandomFromFile(NegativesGeneralDir,False)
                        NegativeTagsFinal = NegativeTagsFinal + RandomFromFile(NegativesBWDir,False)
                    elif(NegativeTags == "general+character"):
                        NegativeTagsFinal = RandomFromFile(NegativesGeneralDir,False)
                        NegativeTagsFinal = NegativeTagsFinal + RandomFromFile(NegativesCharacterDir,False)
                    elif(NegativeTags == "general+character+B&W"):
                        NegativeTagsFinal = RandomFromFile(NegativesGeneralDir,False)
                        NegativeTagsFinal = NegativeTagsFinal  + RandomFromFile(NegativesCharacterDir,False)
                        NegativeTagsFinal = NegativeTagsFinal  + RandomFromFile(NegativesBWDir,False)


                # Style Lora 
                # < lora : name : strenght > 
                # [Strenght] -> slider value
                if ddStyleLora != "Not set":
                    if ddStyleLora == "Random":
                        StyleLora = random.choice(RandomFromFile(StyleDir,False))
                        if (slStyleLoraStrength == 1.0):
                            StyleLoraResult = StyleLora.replace("*","") + " "
                        else :
                            # Find the last occurrence of ':'
                            last_colon_index = StyleLora.rfind(':')
                            StyleLoraResult = " (" + StyleLora[:last_colon_index + 1] + str(slStyleLoraStrength) + ") "
                        StyleLoraPositives = GetPromptsFromFile(StyleDir,StyleLora,True)
                        StyleLoraNegatives = GetPromptsFromFile(StyleDir,StyleLora,False)
                    elif ddStyleLora == "Random From Favs":
                        StyleLora = random.choice(RandomFromFile(StyleDir,True))
                        if (slStyleLoraStrength == 1.0):
                            StyleLoraResult = StyleLora.replace("*","") + " "
                        else :
                            last_colon_index = StyleLora.rfind(':')
                            StyleLoraResult = " (" + StyleLora[:last_colon_index + 1] + str(slStyleLoraStrength) + ") "
                        StyleLoraPositives = GetPromptsFromFile(StyleDir,StyleLora,True)
                        StyleLoraNegatives = GetPromptsFromFile(StyleDir,StyleLora,False)
                    else:
                        StyleLora = ddStyleLora.replace("*","")
                        StyleLoraPositives = GetPromptsFromFile(StyleDir,StyleLora,True)
                        StyleLoraNegatives = GetPromptsFromFile(StyleDir,StyleLora,False)
                        if (slStyleLoraStrength == 1.0):
                            StyleLoraResult = StyleLora  + " "
                        else :    
                            last_colon_index = StyleLora.rfind(':')
                            StyleLoraResult = " (" + StyleLora[:last_colon_index + 1] + str(slStyleLoraStrength) + ") "


                # Style Embedding TO-DO promeniti ime i spojiti u Combine_Field_With_Slider

                result = Combine_Field_With_Slider(ddStyleEmbedding,slStyleEmbeddingStrength,StyleEmbedding,StyleEmbeddingDir,StyleEmbeddingPositives,StyleEmbeddingNegatives,StyleEmbeddingResult)

                StyleEmbedding,StyleEmbeddingPositives,StyleEmbeddingNegatives,StyleEmbeddingResult,slStyleEmbeddingStrength = result 

                # Style 
                result = Combine_Field_With_Slider(ddStyleGeneral,slStyleGeneralStrength,StyleGeneral,StyleDir,StyleGeneralPositives,StyleGeneralNegatives,StyleGeneralResult)

                StyleGeneral,StyleGamePositives,StyleGameNegatives,StyleGeneralResult,slStyleGeneralStrength = result 

                result = Combine_Field_With_Slider(ddStyleGame,slStyleGameStrength,StyleGame,StyleGameDir,StyleGamePositives,StyleGameNegatives,StyleFinal)

                StyleGame,StyleGamePositives,StyleGameNegatives,StyleFinal,slStyleGameStrength = result 


                # Material 
                result = Combine_SubFields_With_Slider(ddMaterial,ddMaterialSub,slMaterialStrength,MaterialPositives,MaterialNegatives,MaterialSubPositives,MaterialSubNegatives,Material,MaterialSub,MaterialResult,MaterialFinal,MaterialDir,MaterialSubDir)

                Material,MaterialSub,MaterialPositives,MaterialNegatives,MaterialSubPositives,MaterialSubNegatives,MaterialResult,MaterialFinal,slMaterialStrength = result 

                # Season && Holiday
                result = Combine_Fields_With_Slider(ddSeason,ddHoliday,slSeasonHolidayStrength,SeasonPositives,SeasonNegatives,HolidayPositives,HolidayNegatives,Season,Holiday,SeasonResult,SeasonHolidayFinal,SeasonDir,HolidayDir)

                Season,Holiday,SeasonPositives,SeasonNegatives,HolidayPositives,HolidayNegatives,SeasonResult,SeasonHolidayFinal,slSeasonHolidayStrength = result 

                # Lighting && SubLight
                result = Combine_SubFields_With_Slider(ddLighting,ddLightingSub,slLightingStrength,LightingPositives,LightingNegatives,LightingSubPositives,LightingSubNegatives,Lighting,LightingSub,LightingResult,LightingFinal,LightingDir,LightingSubDir)

                Lighting,LightingSub,LightingPositives,LightingNegatives,LightingSubPositives,LightingSubNegatives,LightingResult,LightingFinal,slLightingStrength = result 



                # Lighting Effect
 
                result = Combine_Field_With_Slider(ddLightingEffect,slLightingEffectStrength,LightingEffect,LightingEffectDir,LightingEffectPositives,LightingEffectNegatives,LightingEffectResult)

                LightingEffect,LightingEffectPositives,LightingEffectNegatives,LightingEffectResult,slLightingEffectStrength = result 

     
                # Shot Type && ShotAngle 
                result = Combine_Fields_With_Slider(ddCameraShotType,ddCameraShotAngle,slCameraGroup1,CameraShotTypePositives,CameraShotTypeNegatives,CameraShotAnglePositives,CameraShotAngleNegatives,ShotType,ShotAngle,ShotTypeResult,CameraResult1,CameraShotTypeDir,CameraShotAngleDir)

                ShotType,ShotAngle,CameraShotTypePositives,CameraShotTypeNegatives,CameraShotAnglePositives,CameraShotAngleNegatives,ShotTypeResult,CameraResult1,slCameraGroup1 = result 
                

                # Camera Brand && Film Size
                result = Combine_Fields_With_Slider(ddCameraBrand,ddCameraFilmSize,slCameraGroup2,CameraBrandPositives,CameraBrandNegatives,CameraFilmSizePositives,CameraFilmSizeNegatives,ShotBrand,ShotSize,ShotBrandResult,CameraResult2,CameraBrandDir,CameraFilmSizeDir)

                ShotBrand,ShotSize,CameraBrandPositives,CameraBrandNegatives,CameraFilmSizePositives,CameraFilmSizeNegatives,ShotBrandResult,CameraResult2,slCameraGroup2 = result


                # Camera Focal Len && Focus
                result = Combine_Fields_With_Slider(ddCameraFocus,ddCameraFocalLength,slCameraGroup3,CameraFocusPositives,CameraFocusNegatives,CameraFocalLenPositives,CameraFocalLenNegatives,ShotFocus,ShotFocalLen,ShotFocusResult,CameraResult3,CameraFocusDir,CameraFocalLenDir)

                ShotFocus,ShotFocalLen,CameraFocusPositives,CameraFocusNegatives,CameraFocalLenPositives,CameraFocalLenNegatives,ShotFocusResult,CameraResult3,slCameraGroup3 = result


                # PhotographyType && Photographers 
                result = Combine_SubFields_With_Slider(ddPhotographyType,ddPhotographers,slPhotographyStrenght,PhotographyTypePositives,PhotographyTypeNegatives,PhotographersPositives,PhotographersNegatives,PhotographyType,Photographers,PhotographyTypeResult,PhotographyFinal,PhotographyTypeDir,PhotographersDir)

                PhotographyType,Photographers,PhotographyTypePositives,PhotographyTypeNegatives,PhotographersPositives,PhotographersNegatives,PhotographyTypeResult,PhotographyFinal,slPhotographyStrenght = result 
               
                 #artists
                #ArtistResult
                result = Combine_Fields_With_Slider(ddArtistSingle,ddArtistSimilar,slArtistGroupStrength,SingleArtistPositives,SingleArtistNegatives,ArtistThemePositives,ArtistThemeNegatives,SingleArtist,ArtistTheme,SingleArtistResult,ArtistsFinal,ArtistSingleDir,ArtistThemeDir)

                SingleArtist,ArtistTheme,SingleArtistPositives,SingleArtistNegatives,ArtistThemePositives,ArtistThemeNegatives,SingleArtistResult,ArtistsFinal,slArtistGroupStrength = result 
                        

                result = Combine_Fields_With_Slider(ddColorTone,ddColorScheme,slResultColorStrength,ColorTonePositives,ColorToneNegatives,ColorSchemePositives,ColorSchemeNegatives,ColorTone,ColorScheme,ColorToneResult,FinalResultColor,ColorsTonesDir,ColorsSchemesDir) 

                ColorTone,ColorScheme,ColorTonePositives,ColorToneNegatives,ColorSchemePositives,ColorSchemeNegatives,ColorToneResult,FinalResultColor,slResultColorStrength = result 
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->
               
               
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->


                # FEMALE CHARACTER

                # Beauty Desc && Content Rating
                #result = Combine_Fields_With_Slider(ddBeautyDescriptor,ddContentRating,slBeautyStrenght,BeautyDescriptorPositives,BeautyDescriptorNegatives,ContentRatingPositives,ContentRatingNegatives,BeautyDescriptor,ContentRating,BeautyDescResult,ContentRatingResult,BeautyDescriptorDir,ContentRatingDir)

                #BeautyDescriptor,ContentRating,BeautyDescriptorPositives,BeautyDescriptorNegatives,ContentRatingPositives,ContentRatingNegatives,BeautyDescResult,ContentRatingResult,slBeautyStrenght = result

                result = Combine_Field_With_Slider(ddBeautyDescriptor,slBeautyStrenght,BeautyDescriptor,BeautyDescriptorDir,BeautyDescriptorPositives,BeautyDescriptorNegatives,BeautyDescResult)

                BeautyDescriptor,BeautyDescriptorPositives,BeautyDescriptorNegatives,BeautyDescResult,slBeautyStrenght = result 

                # Content rating 
                result = Combine_Field_With_Slider(ddContentRating,slBeautyStrenght,ContentRating,ContentRatingDir,ContentRatingPositives,ContentRatingNegatives,ContentRatingResult)

                ContentRating,ContentRatingPositives,ContentRatingNegatives,ContentRatingResult,slBeautyStrenght = result 

                # Female Type 
                result = Combine_SubFields_With_Slider(ddFemaleType,ddSpecificPerson,slFemaleTypeStrenght,FemaleTypePositives,FemaleTypeNegatives,SpecificPersonPositives,SpecificPersonNegatives,FemaleType,SpecificPerson,FemaleTypeResult,FemaleTypeFinal,FemaleTypeDir,SpecificPersonDir)

                FemaleType,SpecificPerson,FemaleTypePositives,FemaleTypeNegatives,SpecificPersonPositives,SpecificPersonNegatives,FemaleTypeResult,FemaleTypeFinal,slFemaleTypeStrenght = result 

                # Goddess 
                result = Combine_SubFields_With_Slider(ddGoddessType,ddGoddess,slGoddessStrenght,GoddessTypePositives,GoddessTypeNegatives,GoddessPositives,GoddessNegatives,GoddessType,Goddess,GoddessTypeResult,GoddessFinal,GoddessTypeDir,GoddessDir)

                GoddessType,Goddess,GoddessTypePositives,GoddessTypeNegatives,GoddessPositives,GoddessNegatives,GoddessTypeResult,GoddessFinal,slGoddessStrenght  = result 
                # Formating output 
                if Goddess != "" and GoddessType != "":
                    if (slGoddessStrenght != 1.0):
                        GoddessFinal = "(" + Goddess + ", " + GoddessType + ": " + str(slGoddessStrenght) + ") "
                    else :
                        GoddessFinal = Goddess  + ", " + GoddessType  

                # Embedding 
                result = Combine_Field_With_Slider(ddEmbedding,slCelebrityEmbedding,Embedding,EmbeddingDir,EmbeddingPositives,EmbeddingNegatives,CelebrityEmbeddingFinal)

                Embedding,EmbeddingPositives,EmbeddingNegatives,CelebrityEmbeddingFinal,slCelebrityEmbedding = result

                # Lora  
                # <lora : name : strenght >  
                # [Strenght] -> slider value     
                if ddLora != "Not set":
                    if ddLora == "Random":
                        Lora = random.choice(RandomFromFile(LoraDir,False))
                        if (slLoraStrenght == 1.0):
                            LoraResult = Lora.replace("*","") + " "
                        else :
                            # Find the last occurrence of ':'
                            last_colon_index = Lora.rfind(':')
                            LoraResult = " (" + Lora[:last_colon_index + 1] + str(slLoraStrenght) + ") "
                        LoraNegatives = GetPromptsFromFile(LoraDir,Lora,False)
                    elif ddLora == "Random From Favs":
                        Lora = random.choice(RandomFromFile(LoraDir,True))
                        if (slLoraStrenght == 1.0):
                            LoraResult = Lora.replace("*","") + " "
                        else :
                            last_colon_index = Lora.rfind(':')
                            LoraResult = " (" + Lora[:last_colon_index + 1] + str(slLoraStrenght) + ") "
                        LoraPositives = GetPromptsFromFile(LoraDir,Lora,True)
                        LoraNegatives = GetPromptsFromFile(LoraDir,Lora,False)
                    else:
                        Lora = ddLora.replace("*","")
                        LoraPositives = GetPromptsFromFile(LoraDir,Lora,True)
                        LoraNegatives = GetPromptsFromFile(LoraDir,Lora,False)
                        if (slLoraStrenght == 1.0):
                            LoraResult = Lora  + " "
                        else :    
                            last_colon_index = Lora.rfind(':')
                            LoraResult = " (" + Lora[:last_colon_index + 1] + str(slLoraStrenght) + ") "


                # OriginOrNationality && Skin Color 
                result = Combine_Fields_With_Slider(ddOriginOrNationality,ddSkinColor,slOriginColorStrenght,OriginOrNationalityPositives,OriginOrNationalityNegatives,SkinColorPositives,SkinColorNegatives,OriginOrNationality,SkinColor,OriginOrNationalityResult,OriginColorFinal,OriginOrNationalityDir,SkinColorDir)

                OriginOrNationality,SkinColor,OriginOrNationalityPositives,OriginOrNationalityNegatives,SkinColorPositives,SkinColorNegatives,OriginOrNationalityResult,OriginColorFinal,slOriginColorStrenght = result
 

                # BodyView && Camera Angle 
                result = Combine_Fields_With_Slider(ddBodyView,ddCameraAngle,slBodyAngleStrenght,BodyViewPositives,BodyViewNegatives,CameraAnglePositives,CameraAngleNegatives,BodyView,CameraAngle,BodyViewResult,BodyAngleFinal,BodyViewDir,CameraAngleDir)

                BodyView,CameraAngle,BodyViewPositives,BodyViewNegatives,CameraAnglePositives,CameraAngleNegatives,BodyViewResult,BodyAngleFinal,slBodyAngleStrenght = result

                # Looking Where && Camera Focus 
                result = Combine_Fields_With_Slider(ddLookingWhere,ddCameraFFocus,slCameraLookingWhereStrenght,LookingWherePositives,LookingWhereNegatives,CameraFocusPositives,CameraFocusNegatives,LookingWhere,CameraFocus,LookingWhereResult,CameraLookingFinal,LookingWhereDir,CameraFFocusDir)

                LookingWhere,CameraFocus,LookingWherePositives,LookingWhereNegatives,CameraFocusPositives,CameraFocusNegatives,LookingWhereResult,CameraLookingFinal,slCameraLookingWhereStrenght = result

                # ===================================================================================
                # Head 
                # FaceShpe && FaceExpression
                result = Combine_Fields_With_Slider(ddFaceShape,ddFaceExpression,slShapeExpressionStrenght,FaceShapePositives,FaceShapeNegatives,FaceExpressionPositives,FaceExpressionNegatives,FaceShape,FaceExpression,ShapeResult,ShapeExpressionFinal,FaceShapeDir,FaceExpressionDir)

                FaceShape,FaceExpression,FaceShapePositives,FaceShapeNegatives,FaceExpressionPositives,FaceExpressionNegatives,ShapeResult,ShapeExpressionFinal,slShapeExpressionStrenght = result 

                # Hair Color && Hair Cut 
                result = Combine_Fields_With_Slider(ddHairColor,ddHairCut,slColorCutStrenght,HairColorPositives,HairColorNegatives,HairCutPositives,HairCutNegatives,HairColor,HairCut,ColorResult,ColorCutFinal,HairColorDir,HairCutDir)

                HairColor,HairCut,HairColorPositives,HairColorNegatives,HairCutPositives,HairCutNegatives,ColorResult,ColorCutFinal,slColorCutStrenght = result 

                # Eye Color && Eye Shape
                result = Combine_Fields_With_Slider(ddEyeColor,ddEyeShape,slColorShapeStrenght,EyeColorPositives,EyeColorNegatives,EyeShapePositives,EyeShapeNegatives,EyeColor,EyeShape,EyeResult,EyeFinal,EyeColorDir,EyeShapeDir)

                EyeColor,EyeShape,EyeColorPositives,EyeColorNegatives,EyeShapePositives,EyeShapeNegatives,EyeResult,EyeFinal,slColorShapeStrenght = result

                # Eyebrows && Nose 
                result = Combine_Fields_With_Slider(ddEyeBrows,ddNose,slBrowsNoseStrenght,EyeBrowsPositives,EyeBrowsNegatives,NosePositives,NoseNegatives,EyeBrows,Nose,BrowsResult,BrowsNoseFinal,EyeBrowsDir,NoseDir)

                EyeBrows,Nose,EyeBrowsPositives,EyeBrowsNegatives,NosePositives,NoseNegatives,BrowsResult,BrowsNoseFinal,slBrowsNoseStrenght = result 

                # Lips && Chin
                result = Combine_Fields_With_Slider(ddLips,ddChin,slLipsChinStrenght,LipPositives,LipNegatives,ChinPositives,ChinNegatives,Lips,Chin,LipResult,LipChinFinal,LipsDir,ChinDir)

                Lips,Chin,LipPositives,LipNegatives,ChinPositives,ChinNegatives,LipResult,LipChinFinal,slLipsChinStrenght = result 


                # =========================================================================                    
                # Head Accessories

                # HairAccessories && Animal Ears 
                result = Combine_Fields_With_Slider(ddHairAccessories,ddAnimalEars,slHairEarsStrenght,HairAccessoryPositives,HairAccessoryNegatives,AnimalEarsPositives,AnimalEarsNegatives,HairAccessory,AnimalEars,HairAccessoryResult,HairEarsFinal,HairAccessoryDir,AnimalEarsDir)

                HairAccessory,AnimalEars,HairAccessoryPositives,HairAccessoryNegatives,AnimalEarsPositives,AnimalEarsNegatives,HairAccessoryResult,HairEarsFinal,slHairEarsStrenght = result

                # Earrings && Neckless + slider
                result = Combine_Fields_With_Slider(ddEarrings,ddNeckless,slEarringsNecklessStrenght,EarringsPositives,EarringsNegatives,NecklessPositives,NecklessNegatives,Earrings,Neckless,EarringsResult,EarringsNecklessFinal,EarringsDir,NecklessDir)

                Earrings,Neckless,EarringsPositives,EarringsNegatives,NecklessPositives,NecklessNegatives,EarringsResult,EarringsNecklessFinal,slEarringsNecklessStrenght = result

                # Hat && Glasses + slider
                result = Combine_Fields_With_Slider(ddHat,ddGlasses,slHatGlassesStrenght,HatPositives,HatNegatives,GlassesPositives,GlassesNegatives,Hat,Glasses,HatResult,HatGlassesFinal,HatDir,GlassesDir)
                
                Hat,Glasses,HatPositives,HatNegatives,GlassesPositives,GlassesNegatives,HatResult,HatGlassesFinal,slHatGlassesStrenght = result

                # QuickBackGround 
                result = Combine_Field_With_Slider(ddQuickBackGround,slBackGroundStrenght,QuickBackGround,QuickBackGroundDir,QuickBackGroundPositives,QuickBackGroundNegatives,QuickBackGroundResult)

                QuickBackGround,QuickBackGroundPositives,QuickBackGroundNegatives,QuickBackGroundResult,slBackGroundStrenght = result                        

                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                # BodyType
                result = Combine_Field_With_Slider(ddBodyType,slBodyTypeStrenght,BodyType,BodyTypeDir,BodyTypePositives,BodyTypeNegatives,BodyTypeFinal)

                BodyType,BodyTypePositives,BodyTypeNegatives,BodyTypeFinal,slBodyTypeStrenght = result 


                # Age && Skin 
                result = Combine_Fields_With_Slider(ddAge,ddSkin,slAgeSkinStrenght,AgePositives,AgeNegatives,SkinPositives,SkinNegatives,Age,Skin,AgeResult,SkinResult,AgeDir,SkinDir)

                Age,Skin,AgePositives,AgeNegatives,SkinPositives,SkinNegatives,AgeResult,SkinResult,slAgeSkinStrenght = result 

                # Breast Size && Breast Desc + slider
                result = Combine_Fields_With_Slider(ddBreastSize,ddBreastDesc,slBreastStrenght,BreastSizePositives,BreastSizeNegatives,BreastDescriptorPositives,BreastDescriptorNegatives,BreastSize,BreastDescriptor,BreastSizeResult,BreastFinal,BreastSizeDir,BreastDescriptorDir)
                
                BreastSize,BreastDescriptor,BreastSizePositives,BreastSizeNegatives,BreastDescriptorPositives,BreastDescriptorNegatives,BreastSizeResult,BreastFinal,slBreastStrenght = result 


                # Ass Size && Ass Desc + slider
                result = Combine_Fields_With_Slider(ddAssSize,ddAssDesc,slAssStrenght,AssSizePositives,AssSizeNegatives,AssDescriptorPositives,AssDescriptorNegatives,AssSize,AssDescriptor,AssSizeResult,AssFinal,AssSizeDir,AssDescriptorDir)
                
                AssSize,AssDescriptor,AssSizePositives,AssSizeNegatives,AssDescriptorPositives,AssDescriptorNegatives,AssSizeResult,AssFinal,slAssStrenght = result 

                # Hips / Legs Descriptor 
                result = Combine_Fields_With_Slider(ddHips,ddLegsDesc,slHipsLegsStrenght,HipsPositives,HipsNegatives,LegsDescriptorPositives,LegsDescriptorNegatives,Hips,LegsDescriptor,HipsResult,HipsLegsFinal,HipsDir,LegsDescriptorDir)

                Hips,LegsDescriptor,HipsPositives,HipsNegatives,LegsDescriptorPositives,LegsDescriptorNegatives,HipsResult,HipsLegsFinal,slHipsLegsStrenght = result

                # Wardrobe && SubType
                    
                result = Combine_SubFields_With_Slider(ddWardrobe,ddWardrobeSub,slWardrobeStrenght,WardrobePositives,WardrobeNegatives,WardrobeSubPositives,WardrobeSubNegatives,Wardrobe,WardrobeSub,WardrobeResult,WardrobeFinal,WardrobeDir,WardrobeSubDir)
               
                Wardrobe,WardrobeSub,WardrobePositives,WardrobeNegatives,WardrobeSubPositives,WardrobeSubNegatives,WardrobeResult,WardrobeFinal,slWardrobeStrenght = result 

                # Footwear && SubType
                result = Combine_SubFields_With_Slider(ddFootwear,ddFootwearSub,slFootwearStrenght,FootwearPositives,FootwearNegatives,FootwearSubPositives,FaceShapeNegatives,Footwear,FootwearSub,FootwearResult,FootwearFinal,FootwearDir,FootwearSubDir)

                Footwear,FootwearSub,FootwearPositives,FootwearNegatives,FootwearSubPositives,FootwearSubNegatives,FootwearResult,FootwearFinal,slFootwearStrenght = result 

                # Female Body Armor
                result = Combine_Field_With_Slider(ddFemaleFullBodyArmor,slFemaleFullBodyArmorStrenght,FemaleBodyArmor,FemaleBodyArmorDir,FemaleBodyArmorPositives,FemaleBodyArmorNegatives,FemaleBodyArmorResult)

                FemaleBodyArmor,FemaleBodyArmorPositives,FemaleBodyArmorNegatives,FemaleBodyArmorResult,slFemaleFullBodyArmorStrenght = result 


                # Head / Neck Armor
                result = Combine_Fields_With_Slider(ddFemaleHeadArmor,ddFemaleNeckArmor,slFemaleHeadNeckStrenght,FemaleHeadArmorPositives,FemaleHeadArmorNegatives,FemaleNeckArmorPositives,FemaleNeckArmorNegatives,FemaleHeadArmor,FemaleNeckArmor,FemaleHeadArmorResult,FemaleHeadNeckFinal,FemaleHeadProtectionDir,FemaleNeckProtectionDir)

                FemaleHeadArmor,FemaleNeckArmor,FemaleHeadArmorPositives,FemaleHeadArmorNegatives,FemaleNeckArmorPositives,FemaleNeckArmorNegatives,FemaleHeadArmorResult,FemaleHeadNeckFinal,slFemaleHeadNeckStrenght = result 


                # Shoulders / Chest
                result = Combine_Fields_With_Slider(ddFemaleShoulderArmor,ddFemaleChestArmor,slFemaleShoulderChestStrenght,FemaleShoulderArmorPositives,FemaleShoulderArmorNegatives,FemaleChestArmorPositives,FemaleChestArmorNegatives,FemaleShoulderArmor,FemaleChestArmor,FemaleShoulderArmorResult,FemaleShoulderChestFinal,FemaleShoulderProtectionDir,FemaleTorsoProtectionDir)

                FemaleShoulderArmor,FemaleChestArmor,FemaleShoulderArmorPositives,FemaleShoulderArmorNegatives,FemaleChestArmorPositives,FemaleChestArmorNegatives,FemaleShoulderArmorResult,FemaleShoulderChestFinal,slFemaleShoulderChestStrenght = result 

                # Legs / Groin
                result = Combine_Fields_With_Slider(ddFemaleShoulderArmor,ddFemaleChestArmor,slFemaleLegGroinStrenght,FemaleLegArmorPositives,FemaleLegArmorNegatives,FemaleGroinArmorPositives,FemaleGroinArmorNegatives,FemaleLegArmor,FemaleGroinArmor,FemaleLegArmorResult,FemaleLegGroinFinal,FemaleLegProtectionDir,FemaleGroinProtectionDir)
                
                FemaleLegArmor,FemaleGroinArmor,FemaleLegArmorPositives,FemaleLegArmorNegatives,FemaleGroinArmorPositives,FemaleGroinArmorNegatives,FemaleLegArmorResult,FemaleLegGroinFinal,slFemaleLegGroinStrenght = result 


                # Weapon / subtype
                result = Combine_SubFields_With_Slider(ddFemaleWeapons,ddFemaleWeaponsSub,slFemaleWeaponsStrenght,FemaleWeaponPositives,FemaleWeaponNegatives,FemaleWeaponSubPositives,FemaleWeaponSubNegatives,FemaleWeapon,FemaleWeaponSub,FemaleWeaponResult,FemaleWeaponsFinal,FemaleWeaponDir,FemaleWeaponSubmenuDir) 
                
                FemaleWeapon,FemaleWeaponSub,FemaleWeaponPositives,FemaleWeaponNegatives,FemaleWeaponSubPositives,FemaleWeaponSubNegatives,FemaleWeaponResult,FemaleWeaponsFinal,slFemaleWeaponsStrenght = result 

                # Shield 
                result = Combine_Field_With_Slider(ddFemaleShield,slFemaleShield,FemaleShield,FemaleShieldDir,FemaleShieldPositives,FemaleShieldNegatives,FemaleShieldFinal)

                FemaleShield,FemaleShieldPositives,FemaleShieldNegatives,FemaleShieldFinal,slFemaleShield = result 
                # =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=->

                #  Male Character 
                # Content Rating && Beautifier

                result = Combine_Field_With_Slider(ddMaleBeautyDescriptor,slMaleContent,MaleBeautyDescriptor,MaleBeautifiersDir,MaleBeautyDescriptorPositives,MaleBeardNegatives,MaleRatingDescFinal)

                MaleBeautyDescriptor,MaleBeautyDescriptorPositives,MaleBeardNegatives,MaleRatingDescFinal,slMaleContent = result 

                result = Combine_Field_With_Slider(ddMaleContentRating,slMaleContent,MaleContentRating,MaleContentRatingDir,MaleEyeColorPositives,MaleEyeColorNegatives,MaleContentRatingResult)

                MaleContentRating,MaleContentRatingPositives,MaleContentRatingNegatives,MaleContentRatingResult,slMaleContent = result 


                # Male Type && SubType 
                result = Combine_SubFields_With_Slider(ddMaleType,ddMaleSubType,slMaleTypeStrenght,MaleTypePositives,MaleTypeNegatives,MaleSubTypePositives,MaleSubTypeNegatives,MaleType,MaleSubType,MaleTypeResult,MaleTypeFinal,MaleTypeDir,MaleSubTypeDir)
 
                MaleType,MaleSubType,MaleTypePositives,MaleTypeNegatives,MaleSubTypePositives,MaleSubTypeNegatives,MaleTypeResult,MaleTypeFinal,slMaleTypeStrenght = result
                
                # God Type && God  
                result = Combine_SubFields_With_Slider(ddMaleGodType,ddMaleGod,slMaleGodStrenght,MaleGodTypePositives,MaleGodTypeNegatives,MaleGodPositives,MaleGodNegatives,MaleGodType,MaleGod,MaleGodTypeResult,MaleGodFinal,MaleGodTypeDir,MaleGodDir)

                MaleGodType,MaleGod,MaleGodTypePositives,MaleGodTypeNegatives,MaleGodPositives,MaleGodNegatives,MaleGodTypeResult,MaleGodFinal,slMaleGodStrenght  = result 
                # Formating the final value
                if MaleGod != "" and MaleGodType != "":
                    if ( slMaleGodStrenght != 1.0):
                        MaleGodFinal = "(" + MaleGod + ", " + MaleGodType + ": " + str(slMaleGodStrenght) + ") "
                    else :
                        MaleGodFinal = MaleGod + ", " + MaleGodType 
                
                # Embedding
                result = Combine_Field_With_Slider(ddMaleEmbedding,slMaleEmbeddingStrenght,MaleEmbedding,MaleEmbeddingsDir,MaleEmbeddingPositives,MaleEmbeddingNegatives,MaleEmbeddingResult)

                MaleEmbedding,MaleEmbeddingPositives,MaleEmbeddingNegatives,MaleEmbeddingResult,slMaleEmbeddingStrenght = result 

                # Lora
                # <lora : name : strenght >  
                # [Strenght] -> slider value
                if ddMaleLora != "Not set":
                    if ddMaleLora == "Random":
                        MaleLora = random.choice(RandomFromFile(MaleLoraDir,False))
                        if (slMaleLoraStrenght == 1.0):
                            MaleLoraResult = MaleLora.replace("*","") + " "
                        else :
                            # Find the last occurrence of ':'
                            last_colon_index = MaleLora.rfind(':')
                            MaleLoraResult = " (" + MaleLora[:last_colon_index + 1] + str(slMaleLoraStrenght) + ") "
                        MaleLoraPositives = GetPromptsFromFile(MaleLoraDir,MaleLora,True)
                        MaleLoraNegatives = GetPromptsFromFile(MaleLoraDir,MaleLora,False)
                    elif ddMaleLora == "Random From Favs":
                        MaleLora = random.choice(RandomFromFile(MaleLoraDir,True))
                        if (slMaleLoraStrenght == 1.0):
                            MaleLoraResult = MaleLora.replace("*","") + " "
                        else :
                            last_colon_index = MaleLora.rfind(':')
                            MaleLoraResult = " (" + MaleLora[:last_colon_index + 1] + str(slMaleLoraStrenght) + ") "
                        MaleLoraPositives = GetPromptsFromFile(MaleLoraDir,MaleLora,True)
                        MaleLoraNegatives = GetPromptsFromFile(MaleLoraDir,MaleLora,False)
                    else:
                        MaleLora = ddMaleLora.replace("*","")
                        MaleLoraPositives = GetPromptsFromFile(MaleLoraDir,MaleLora,True)
                        MaleLoraNegatives = GetPromptsFromFile(MaleLoraDir,MaleLora,False)
                        if (slMaleLoraStrenght == 1.0):
                            MaleLoraResult = MaleLora  + " "
                        else :    
                            last_colon_index = MaleLora.rfind(':')
                            MaleLoraResult = " (" + MaleLora[:last_colon_index + 1] + str(slMaleLoraStrenght) + ") "


                # Origin && Skin Color
                result = Combine_Fields_With_Slider(ddMaleOrigin,ddMaleSkinColor,slMaleOriginSkinStrenght,MaleOriginOrNationalityPositives,MaleOriginOrNationalityNegatives,MaleSkinColorPositives,MaleSkinColorNegatives,MaleOriginOrNationality,MaleSkinColor,MaleOriginOrNationalityResult,MaleOriginColorFinal,MaleOriginOrNationalityDir,MaleSkinColorDir)

                MaleOriginOrNationality,MaleSkinColor,MaleOriginOrNationalityPositives,MaleOriginOrNationalityNegatives,MaleSkinColorPositives,MaleSkinColorNegatives,MaleOriginOrNationalityResult,MaleOriginColorFinal,slMaleOriginSkinStrenght = result

                # Body View && Body Angle
                result = Combine_Fields_With_Slider(ddMaleBodyView,ddMaleBodyAngle,slMaleBodyAngleStrenght,MaleBodyViewPositives,MaleBodyViewNegatives,MaleBodyAnglePositives,MaleBodyAngleNegatives,MaleBodyView,MaleBodyAngle,MaleBodyViewResult,MaleViewAngleFinal,MaleBodyViewDir,MaleBodyAngleDir)

                MaleBodyView,MaleBodyAngle,MaleBodyViewPositives,MaleBodyViewNegatives,MaleBodyAnglePositives,MaleBodyAngleNegatives,MaleBodyViewResult,MaleViewAngleFinal,slBodyAngleStrenght = result
                
                # Camera Focus && Looking Where
                result = Combine_Fields_With_Slider(ddMaleCameraFocus,ddMaleLooking,slMaleFocusLooking,MaleBodyFocusPositives,MaleBodyFocusNegatives,MaleLookingWherePositives,MaleLookingWhereNegatives,MaleBodyFocus,MaleLookingWhere,MaleLookingWhereResult,MaleLookingFocusFinal,MaleCameraFocusDir,MaleLookingWhereDir)

                MaleBodyFocus,MaleLookingWhere,MaleBodyFocusPositives,MaleBodyFocusNegatives,MaleLookingWherePositives,MaleLookingWhereNegatives,MaleLookingWhereResult,MaleLookingFocusFinal,slMaleFocusLooking = result

                # Body Type && Body Height
                result = Combine_Fields_With_Slider(ddMaleBodyType,ddMaleBodyHeight,slBodyHeightStrenght,MaleBodyTypePositives,MaleBodyTypeNegatives,MaleBodyHeightPositives,MaleBodyHeightNegatives,MaleBodyType,MaleBodyHeight,MaleBodyTypeResult,MaleTypeHeightFinal,MaleBodyTypeDir,MaleBodyHeightDir)

                MaleBodyType,MaleBodyHeight,MaleBodyTypePositives,MaleBodyTypeNegatives,MaleBodyHeightPositives,MaleBodyHeightNegatives,MaleBodyTypeResult,MaleTypeHeightFinal,slBodyHeightStrenght = result 

                # Age && Skin
                result = Combine_Fields_With_Slider(ddMaleAge,ddMaleSkin,slMaleAgeSkinStrenght,MaleAgePositives,MaleAgeNegatives,MaleSkinPositives,MaleSkinNegatives,MaleAge,MaleSkin,MaleAgeResult,MaleAgeSkinFinal,MaleAgeDir,MaleSkinDir)

                MaleAge,MaleSkin,MaleAgePositives,MaleAgeNegatives,MaleSkinPositives,MaleSkinNegatives,MaleAgeResult,MaleAgeSkinFinal,slAgeSkinStrenght = result 

                # Wardrobe 
                result = Combine_SubFields_With_Slider(ddMaleWardrobe,ddMaleWardrobeSub,slMaleWardrobeStrenght,MaleWardrobePositives,MaleWardrobeNegatives,MaleWardrobeSubPositives,MaleWardrobeSubNegatives,MaleWardrobe,MaleWardrobeSub,MaleWardrobeResult,MaleWardrobeFinal,MaleWardrobeDir,MaleWardorbeSubDir)

                MaleWardrobe,MaleWardrobeSub,MaleWardrobePositives,MaleWardrobeNegatives,MaleWardrobeSubPositives,MaleWardrobeSubNegatives,MaleWardrobeResult,MaleWardrobeFinal,slMaleWardrobeStrenght = result 
                
                # Footwear
                result = Combine_SubFields_With_Slider(ddMaleFootwear,ddMaleFootwearSub,slMaleFootwearStrenght,MaleFootwearPositives,MaleFootwearNegatives,MaleFootwearSubPositives,MaleFootwearSubNegatives,MaleFootwear,MaleFootwearSub,MaleFootwearResult,MaleFootwearFinal,MaleFootwearDir,MaleFootwearSubDir) 
                
                MaleFootwear,MaleFootwearSub,MaleFootwearPositives,MaleFootwearNegatives,MaleFootwearSubPositives,MaleFootwearSubNegatives,MaleFootwearResult,MaleFootwearFinal,slMaleFootwearStrenght = result 
                
                # FaceShape && FaceExpression
                result = Combine_Fields_With_Slider(ddMaleFaceShape,ddMaleFaceExpression,slMaleShapeExpressionStrenght,MaleFaceShapePositives,MaleFaceShapeNegatives,MaleFaceExpressionPositives,MaleFaceExpressionNegatives,MaleFaceShape,MaleFaceExpression,MaleFaceShapeResult,MaleShapeExpressionFinal,MaleFaceShapeDir,MaleFaceExpressionDir)

                MaleFaceShape,MaleFaceExpression,MaleFaceShapePositives,MaleFaceShapeNegatives,MaleFaceExpressionPositives,MaleFaceExpressionNegatives,MaleFaceShapeResult,MaleShapeExpressionFinal,slMaleShapeExpressionStrenght = result

                # HairColor && HairCut
                result = Combine_Fields_With_Slider(ddMaleHairColor,ddMaleHairCut,slMaleColorCutStrenght,MaleHairColorPositives,MaleHairColorNegatives,MaleHairCutPositives,MaleHairCutNegatives,MaleHairColor,MaleHairCut,MaleHairColorResult,MaleHairFinal,MaleHairColorDir,MaleHairCutDir)

                MaleHairColor,MaleHairCut,MaleHairColorPositives,MaleHairColorNegatives,MaleHairCutPositives,MaleHairCutNegatives,MaleHairColorResult,MaleHairFinal,slMaleColorCutStrenght = result 

                # EyeColor && EyeShape 
                result = Combine_Fields_With_Slider(ddMaleEyeColor,ddMaleEyeShape,slMaleColorShapeStrenght,MaleEyeColorPositives,MaleEyeColorNegatives,MaleEyeShapePositives,MaleEyeShapeNegatives,MaleEyeColor,MaleEyeShape,MaleEyeColorResult,MaleEyesFinal,MaleEyeColorDir,MaleEyeShapeDir)

                MaleEyeColor,MaleEyeShape,MaleEyeColorPositives,MaleEyeColorNegatives,MaleEyeShapePositives,MaleEyeShapeNegatives,MaleEyeColorResult,MaleEyesFinal,slMaleColorShapeStrenght = result 


                # EyeBrows && Glasses
                result = Combine_Fields_With_Slider(ddMaleEyeBrows,ddMaleGlasses,slMaleBrowsGlassesStrenght,MaleEyeBrowsPositives,MaleEyeBrowsNegatives,MaleGlassesPositives,MaleGlassesNegatives,MaleEyeBrows,MaleGlasses,MaleEyeBrowsResult,MaleBrowsGlassesFinal,MaleEyeBrowsDir,MaleGlassesDir)

                MaleEyeBrows,MaleGlasses,MaleEyeBrowsPositives,MaleEyeBrowsNegatives,MaleGlassesPositives,MaleGlassesNegatives,MaleEyeBrowsResult,MaleBrowsGlassesFinal,slMaleBrowsGlassesStrenght = result 


                # Nose && Chin
                result = Combine_Fields_With_Slider(ddMaleNose,ddMaleChin,slMaleNoseChinStrenght,MaleNosePositives,MaleNoseNegatives,MaleChinPositives,MaleChinNegatives,MaleNoseResult,MaleNose,MaleChin,MaleNoseChinFinal,MaleNoseDir,MaleChinDir)

                MaleNose,MaleChin,MaleNosePositives,MaleNoseNegatives,MaleChinPositives,MaleChinNegatives,MaleNoseResult,MaleNoseChinFinal,slMaleNoseChinStrenght = result 


                # Mustache && Beard 
                result = Combine_Fields_With_Slider(ddMustache,ddBeard,slMustacheBeardStrenght,MaleMustachePositives,MaleMustacheNegatives,MaleBeardPositives,MaleBeardNegatives,MaleMustache,MaleBeard,MaleMustacheResult,MaleMustacheBeardFinal,MaleMustacheDir,MaleBeardDir)

                MaleMustache,MaleBeard,MaleMustachePositives,MaleMustacheNegatives,MaleBeardPositives,MaleBeardNegatives,MaleMustacheResult,MaleMustacheBeardFinal,slMustacheBeardStrenght = result 


                # MaleHeadWear && Neckless
                result = Combine_Fields_With_Slider(ddMaleHeadWear,ddMaleNeckless,slMaleNecklessStrenght,MaleHeadWearPositives,MaleHeadWearNegatives,MaleNecklessPositives,MaleNecklessNegatives,MaleHeadWear,MaleNeckless,MaleHeadWearResult,MaleHeadWearFinal,MaleHeadWearDir,MaleNecklessDir)

                MaleHeadWear,MaleNeckless,MaleHeadWearPositives,MaleHeadWearNegatives,MaleNecklessPositives,MaleNecklessNegatives,MaleHeadWearResult,MaleHeadWearFinal,slMaleNecklessStrenght = result 


                # QuickBackGround 
                result = Combine_Field_With_Slider(ddMaleQuickBackGround,slMaleBackGroundStrenght,MaleQuickBackGround,MaleQuickBackGroundDir,MaleQuickBackGroundPositives,MaleQuickBackGroundNegatives,MaleQuickBackGroundResult)

                MaleQuickBackGround,MaleQuickBackGroundPositives,MaleQuickBackGroundNegatives,MaleQuickBackGroundResult,slMaleBackGroundStrenght = result 


                # Male Body Armor
                result = Combine_Field_With_Slider(ddMaleFullBodyArmor,slMaleFullBodyArmorStrenght,MaleBodyArmor,MaleBodyArmorDir,MaleBodyArmorPositives,MaleBodyArmorNegatives,MaleBodyArmorResult)

                MaleBodyArmor,MaleBodyArmorPositives,MaleBodyArmorNegatives,MaleBodyArmorResult,slMaleFullBodyArmorStrenght = result 


                # Head / Neck Armor
                result = Combine_Fields_With_Slider(ddMaleHeadArmor,ddMaleNeckArmor,slMaleHeadNeckStrenght,MaleHeadArmorPositives,MaleHeadArmorNegatives,MaleNeckArmorPositives,MaleNeckArmorNegatives,MaleHeadArmor,MaleNeckArmor,MaleHeadArmorResult,MaleHeadNeckFinal,MaleHeadProtectionDir,MaleNeckProtectionDir)

                MaleHeadArmor,MaleNeckArmor,MaleHeadArmorPositives,MaleHeadArmorNegatives,MaleNeckArmorPositives,MaleNeckArmorNegatives,MaleHeadArmorResult,MaleHeadNeckFinal,slMaleHeadNeckStrenght = result 


                # Shoulders / Chest
                result = Combine_Fields_With_Slider(ddMaleShoulderArmor,ddMaleChestArmor,slMaleShoulderChestStrenght,MaleShoulderArmorPositives,MaleShoulderArmorNegatives,MaleChestArmorPositives,MaleChestArmorNegatives,MaleShoulderArmor,MaleChestArmor,MaleShoulderArmorResult,MaleShoulderChestFinal,MaleShoulderProtectionDir,MaleTorsoProtectionDir)

                MaleShoulderArmor,MaleChestArmor,MaleShoulderArmorPositives,MaleShoulderArmorNegatives,MaleChestArmorPositives,MaleChestArmorNegatives,MaleShoulderArmorResult,MaleShoulderChestFinal,slMaleShoulderChestStrenght = result 

                # Legs / Groin
                result = Combine_Fields_With_Slider(ddMaleShoulderArmor,ddMaleChestArmor,slMaleLegGroinStrenght,MaleLegArmorPositives,MaleLegArmorNegatives,MaleGroinArmorPositives,MaleGroinArmorNegatives,MaleLegArmor,MaleGroinArmor,MaleLegArmorResult,MaleLegGroinFinal,MaleLegProtectionDir,MaleGroinProtectionDir)
                
                MaleLegArmor,MaleGroinArmor,MaleLegArmorPositives,MaleLegArmorNegatives,MaleGroinArmorPositives,MaleGroinArmorNegatives,MaleLegArmorResult,MaleLegGroinFinal,slMaleLegGroinStrenght = result 


                # Weapon / subtype
                result = Combine_SubFields_With_Slider(ddMaleWeapons,ddMaleWeaponsSub,slMaleWeaponsStrenght,MaleWeaponPositives,MaleWeaponNegatives,MaleWeaponSubPositives,MaleWeaponSubNegatives,MaleWeapon,MaleWeaponSub,MaleWeaponResult,MaleWeaponsFinal,MaleWeaponDir,MaleWeaponSubmenuDir) 
                
                MaleWeapon,MaleWeaponSub,MaleWeaponPositives,MaleWeaponNegatives,MaleWeaponSubPositives,MaleWeaponSubNegatives,MaleWeaponResult,MaleWeaponsFinal,slMaleWeaponsStrenght = result 

                # Shield 
                result = Combine_Field_With_Slider(ddMaleShield,slMaleShield,MaleShield,MaleShieldDir,MaleShieldPositives,MaleShieldNegatives,MaleShieldFinal)

                MaleShield,MaleShieldPositives,MaleShieldNegatives,MaleShieldFinal,slMaleShield = result 


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

                print("Beautifiers : "+ Beautifiers + " Details : " + Details  +" Medium Main : " + Medium + " Medium SubType : " + MediumSub  + "HC " + HairColor + "EC " + EyeColor + " MT " + MainType + " CR1 " + CameraResult1 + " CR2 " + CameraResult2 + " CR3 " + CameraResult3)
                print("ArtistResult " + ArtistsFinal + " AllMovements " + AllMovements + " FinalResultColor " + FinalResultColor)
                
                # If main prompt isn't empty...
                
                global buttons


                # Our main prompt composed of all the selected elements

                # Negative Embeddings checkbtns logic

                if ckbutton2  == True:
                     NegativeEmbeddings += " bad_pictures" + ", "
                if ckbutton3  == True:
                     NegativeEmbeddings += "By bad artist -neg" + ", "
                if ckbutton4  == True:
                     NegativeEmbeddings += "FastNegativeV2" + ", "
                if ckbutton5  == True: 
                     NegativeEmbeddings += "Concordant-neg" + ", "
                if ckbutton6  == True:
                     NegativeEmbeddings += "boring_e621_v4" + ", "
                if ckbutton7  == True:
                     NegativeEmbeddings += "UnrealisticDream, BadDream" + ", "
                if ckbutton8  == True:
                     NegativeEmbeddings += "bad-hands-5" + ", "
                if ckbutton9  == True: 
                     NegativeEmbeddings += "badhandv4" + ", "
                if ckbutton10 == True:
                     NegativeEmbeddings += "bad_prompt_versio2-neg" + ", "
                if ckbutton11 == True:
                     NegativeEmbeddings += "negative_hand-neg" + ", "
                if ckbutton12 == True:
                     NegativeEmbeddings += "anime-style-negative-embedding" + ", "
                if ckbutton13 == True:
                     NegativeEmbeddings += "BadDream" + ", "
                if ckbutton14 == True:
                     NegativeEmbeddings += "bad-picture-chill-75v" + ", "
                if ckbutton15 == True:
                     NegativeEmbeddings += "16-token-negative-deliberate-neg" + ", "
                if ckbutton16 == True:
                     NegativeEmbeddings += "realisticvision-negative-embedding" + ", "
                if ckbutton17 == True:
                     NegativeEmbeddings += "badquality" + ", "
                if ckbutton18 == True:
                     NegativeEmbeddings += "JuggernautNegative-neg" + ", "
                if ckbutton19 == True:
                     NegativeEmbeddings += "BeyondNegativev2-neg" + ", "
                if ckbutton20 == True:
                     NegativeEmbeddings += "easynegative" + ", "
                if ckbutton21 == True:
                     NegativeEmbeddings += "ng_deepnegative_v1_75t" + ", "
                if ckbutton22 == True:
                     NegativeEmbeddings += "verybadimagenegative_v1.3" + ", "
                if ckbutton23 == True:
                     NegativeEmbeddings += "FastNegativeV2" + ", "
                if ckbutton24 == True:
                     NegativeEmbeddings += "CyberRealistic_Negative-neg" + ", "


                MainPositive =  ""

                # IF checkbox for positves is true add all positive prompts to main prompt 
                if cbPositives == True:

                    #1 TAB 
                    if  MediumPositives != "" :
                        MediumFinal             = MediumFinal + ", " + MediumPositives 
                    if MediumSubPositives != "" :
                        MediumFinal             = MediumFinal + ", " + MediumSubPositives

                    if BeautifiersPositives != "" :
                        BeautifiersResult = BeautifiersResult + ", " + BeautifiersPositives

                    if StyleLoraPositives != "" :
                        StyleLoraResult         = StyleLoraResult + ", " + StyleLoraPositives
                    if StyleEmbedding != "":
                        StyleEmbeddingResult          = StyleEmbeddingResult  + ", " + StyleEmbedding 

                    if StyleEmbeddingPositives != "" :
                        StyleEmbeddingResult   = StyleEmbeddingResult + ", " + StyleEmbeddingPositives

                    if StyleGeneralPositives != "" : 
                        StyleFinal              = StyleFinal + ", " + StyleGeneralPositives
                    if StyleGamePositives != "" : 
                        StyleGeneralResult      = StyleGeneralResult  + ", " + StyleGamePositives

                    if MaterialPositives != "":
                        MaterialFinal           = MaterialFinal + ", " + MaterialPositives
                    if MaterialPositives != "":
                        MaterialFinal           = MaterialFinal + ", " + MaterialSubPositives 

                    if SeasonPositives != "":                   
                        SeasonHolidayFinal      = SeasonHolidayFinal  + ", " + SeasonPositives
                    if HolidayPositives != "":
                        SeasonHolidayFinal      = SeasonHolidayFinal  + ", " + HolidayPositives

                    if LightingPositives != "":
                        LightingFinal           = LightingFinal + ", " + LightingPositives
                    if LightingSubPositives != "":
                        LightingFinal           = LightingFinal + ", " + LightingSubPositives

                    if LightingEffectPositives != "":
                        LightingEffectResult    = LightingEffectResult + ", " + LightingEffectPositives

                    if ColorSchemePositives != "" :    
                        FinalResultColor        = FinalResultColor + ", " + ColorSchemePositives
                    if ColorSchemePositives != "" :    
                        FinalResultColor        = FinalResultColor + ", " + ColorTonePositives 

                    if SingleArtistPositives != "":                 
                        ArtistsFinal            = ArtistsFinal + ", " + SingleArtistPositives
                    if ArtistThemePositives != "":
                        ArtistsFinal            = ArtistsFinal + ", " + ArtistThemePositives
                    
                    if CameraShotTypePositives != "":
                        CameraResult1           = CameraResult1 + ", " + CameraShotTypePositives
                    if CameraShotAnglePositives != "":
                        CameraResult1           = CameraResult1 + ", " + CameraShotAnglePositives
                    
                    if CameraFilmSizePositives != "":
                        CameraResult2           = CameraResult2 + ", " + CameraFilmSizePositives 
                    if CameraFilmSizePositives != "":
                        CameraResult2           = CameraResult2 + ", " + CameraBrandPositives

                    if CameraFocalLenPositives != "":                      
                        CameraResult3           = CameraResult3 + ", " + CameraFocalLenPositives 
                    if CameraFocusPositives != "":
                        CameraResult3           = CameraResult3 + ", " + CameraFocusPositives

                    if PhotographyTypePositives != "":
                        PhotographyFinal        = PhotographyFinal + ", " + PhotographyTypePositives  
                    if PhotographyTypePositives != "":
                        PhotographyFinal        = PhotographyFinal + ", " + PhotographersPositives 

                    if DetailsPositives != "" :
                        BeautifiersDetailsFinal = BeautifiersDetailsFinal + ", " + DetailsPositives
                        
                    #2 TAB(General) 
                    if ContentRatingPositives != "": 
                        ContentRatingResult     = ContentRatingResult  + ", " + ContentRatingPositives
                    if BeautyDescriptorPositives != "" :
                        BeautyDescResult        = BeautyDescResult     + ", " + BeautyDescriptorPositives

                    if FemaleTypePositives != "" :
                        FemaleTypeFinal         = FemaleTypeFinal  + ", " + FemaleTypePositives
                    if SpecificPersonPositives != "": 
                        FemaleTypeFinal         = FemaleTypeFinal  + ", " + SpecificPersonPositives

                    if GoddessTypePositives != "":
                        GoddessFinal           = GoddessFinal + ", " + GoddessTypePositives
                    if GoddessPositives != "":
                        GoddessFinal           = GoddessFinal + ", " + GoddessPositives

                    if EmbeddingPositives != "" :
                        CelebrityEmbeddingFinal = CelebrityEmbeddingFinal + ", " + EmbeddingPositives

                    if LoraPositives != "" :
                        LoraResult              = LoraResult + ", " + LoraPositives

                    if  OriginOrNationalityPositives != "" :
                        OriginColorFinal        = OriginColorFinal + ", " + OriginOrNationalityPositives
                    if  OriginOrNationalityPositives != "" :
                        OriginColorFinal        = OriginColorFinal + ", " + SkinColorPositives

                    if AgePositives != "" :
                        AgeResult               = AgeResult + ", " + AgePositives
                    
                    if CameraAnglePositives != "" :
                        BodyAngleFinal          = BodyAngleFinal + ", " + CameraAnglePositives
                    if CameraAnglePositives != "" :
                        BodyAngleFinal          = BodyAngleFinal + ", " + BodyViewPositives

                    if LookingWherePositives != "": 
                        CameraLookingFinal      = CameraLookingFinal + ", " + LookingWherePositives
                    if LookingWherePositives != "": 
                        CameraLookingFinal      = CameraLookingFinal + ", " +  CameraFocusPositives


                    #2 TAB(Head)
                    if HairColorPositives != "":
                        ColorCutFinal        = ColorCutFinal + ", " + HairColorPositives
                    if HairCutPositives != "":
                        ColorCutFinal        = ColorCutFinal + ", " + HairCutPositives

                    if EyeColorPositives != "" :
                        EyeFinal             = EyeFinal +  ", "  + EyeColorPositives 
                    if EyeShapePositives != "" :
                        EyeFinal             = EyeFinal  +  ", " + EyeShapePositives

                    if FaceShapePositives != "" :
                        ShapeExpressionFinal = ShapeExpressionFinal + ", " + FaceShapePositives  
                    if FaceExpressionPositives != "" :
                        ShapeExpressionFinal = ShapeExpressionFinal + ", " + FaceExpressionPositives

                    if EyeBrowsPositives != "" :
                        BrowsNoseFinal       = BrowsNoseFinal + ", " + EyeBrowsPositives
                    if NosePositives != "" :
                        BrowsNoseFinal       = BrowsNoseFinal + ", " + NosePositives

                    if LipPositives != "" :
                        LipChinFinal         = LipChinFinal + ", " + LipPositives 
                    if ChinPositives != "" :
                        LipChinFinal         = LipChinFinal + ", " + ChinPositives 

                    #2 TAB(Head Accessories)
                    if HairAccessoryPositives != "" :
                        HairEarsFinal         = HairEarsFinal + ", " + HairAccessoryPositives
                    if AnimalEarsPositives != "":
                        HairEarsFinal         = HairEarsFinal + ", " + AnimalEarsPositives

                    if EarringsPositives != "" :
                        EarringsNecklessFinal = EarringsNecklessFinal + ", " + EarringsPositives  
                    if NecklessPositives != "" :
                        EarringsNecklessFinal = EarringsNecklessFinal + ", " + NecklessPositives 

                    if HatPositives != "" :
                        HatGlassesFinal       = HatGlassesFinal + ", " + HatPositives    
                    if HatPositives != "" :
                        HatGlassesFinal       = HatGlassesFinal + ", " + GlassesPositives 

                    #2 TAB(Body)
                    if BodyTypePositives != "" :
                        BodyTypeFinal         = BodyTypeFinal + ", " + BodyTypePositives

                    if SkinPositives != "" :
                        SkinResult            = SkinResult + ", " + SkinPositives  

                    if BreastSizePositives != "":
                        BreastFinal           = BreastFinal + ", " + BreastSizePositives
                    if BreastSizePositives != "":
                        BreastFinal           = BreastFinal + ", " + BreastDescriptorPositives

                    if AssSizePositives != "" :
                        AssFinal              = AssFinal + ", " + AssSizePositives 
                    if AssSizePositives != "" :
                        AssFinal              = AssFinal + ", " + AssDescriptorPositives

                    if HipsPositives != "" :         
                        HipsLegsFinal         = HipsLegsFinal + ", " + HipsPositives
                    if HipsPositives != "" :         
                        HipsLegsFinal         = HipsLegsFinal + ", " + LegsDescriptorPositives  

                    if WardrobePositives != "" :
                        WardrobeFinal         = WardrobeFinal + ", " +  WardrobePositives
                    if WardrobeSubPositives != "" :
                        WardrobeFinal         = WardrobeFinal + ", " + WardrobeSubPositives

                    if FootwearPositives != "" :
                        FootwearFinal         = FootwearFinal + ", " + FootwearPositives
                    if FootwearPositives != "" :
                        FootwearFinal         = FootwearFinal + ", " + FootwearSubPositives 

                    if QuickBackGroundPositives != "":
                        QuickBackGroundResult = QuickBackGroundResult + QuickBackGroundPositives

                    #2 TAB(RPG)
                    if FemaleBodyArmorPositives != "" :
                        FemaleBodyArmorResult    = FemaleBodyArmorResult    + FemaleBodyArmorPositives

                    if FemaleHeadArmorPositives != "" :
                        FemaleHeadNeckFinal      = FemaleHeadNeckFinal + ", " + FemaleHeadArmorPositives    
                    if FemaleNeckArmorPositives != "" :
                        FemaleHeadNeckFinal      = FemaleHeadNeckFinal + ", " + FemaleNeckArmorPositives

                    if FemaleShoulderArmorPositives != "" :
                        FemaleShoulderChestFinal = FemaleShoulderChestFinal + ", " + FemaleShoulderArmorPositives
                    if FemaleNeckArmorPositives != "" :
                        FemaleShoulderChestFinal = FemaleShoulderChestFinal + ", " + FemaleNeckArmorPositives

                    if FemaleLegArmorPositives != "":
                        FemaleLegGroinFinal      = FemaleLegGroinFinal + ", " + FemaleLegArmorPositives   
                    if FemaleGroinArmorPositives != "":
                        FemaleLegGroinFinal      = FemaleLegGroinFinal + ", " + FemaleGroinArmorPositives
                    
                    if FemaleWeaponPositives != "" :
                        FemaleWeaponsFinal       = FemaleWeaponsFinal + ", " + FemaleWeaponPositives
                    if FemaleWeaponPositives != "" :
                        FemaleWeaponsFinal       = FemaleWeaponsFinal + ", " + FemaleWeaponSubPositives

                    if FemaleShieldPositives != "" :
                        FemaleShieldFinal        = FemaleShieldFinal + ", " + FemaleShieldPositives                     


                    #3 TAB(General)
                    if MaleContentRatingPositives != "" :
                        MaleContentRatingResult   = MaleContentRatingResult  + ", " + MaleContentRatingPositives 
                    if MaleBeautyDescriptorPositives != "":
                        MaleRatingDescFinal       = MaleRatingDescFinal      + ", " + MaleBeautyDescriptorPositives 

                    if MaleTypePositives != "" :
                        MaleTypeFinal         = MaleTypeFinal        + ", " + MaleTypePositives 
                    if MaleSubTypePositives != "" :
                         MaleTypeFinal        = MaleTypeFinal        + ", " + MaleSubTypePositives

                    if MaleGodTypePositives != "":
                        MaleGodFinal           = MaleGodFinal + ", " + MaleGodTypePositives
                    if MaleGodPositives != "":
                        MaleGodFinal           = MaleGodFinal + ", " + MaleGodPositives


                    if MaleEmbeddingPositives != "" :                        
                        MaleEmbeddingResult   = MaleEmbeddingResult   + ", " +  MaleEmbeddingPositives

                    if MaleLoraPositives != "" :                        
                        MaleLoraResult        = MaleLoraResult        + ", " +  MaleLoraPositives 

                    if MaleOriginOrNationalityPositives != "" or  MaleSkinColorPositives != "" :                        
                        MaleOriginColorFinal  = MaleOriginColorFinal  + ", " +  MaleOriginOrNationalityPositives
                    if MaleSkinColorPositives != "" :                        
                        MaleOriginColorFinal  = MaleOriginColorFinal  + ", " + MaleSkinColorPositives

                    if AgePositives != "" :                        
                        AgeResult             = AgeResult             + ", " +  AgePositives

                    if MaleBodyAnglePositives != "" :                        
                        MaleViewAngleFinal    = MaleViewAngleFinal    + ", " + MaleBodyAnglePositives 
                    if MaleBodyViewPositives != "" :                        
                        MaleViewAngleFinal    = MaleViewAngleFinal    + ", " + MaleBodyViewPositives                   

                    if MaleLookingWherePositives != "" :                        
                        MaleLookingFocusFinal = MaleLookingFocusFinal + ", " +  MaleLookingWherePositives 
                    if MaleBodyFocusPositives != "" :                        
                        MaleLookingFocusFinal = MaleLookingFocusFinal + ", " + MaleBodyFocusPositives

                    #3 TAB(Body)
                    if MaleBodyTypePositives != "":
                        MaleTypeHeightFinal = MaleTypeHeightFinal + ", " + MaleBodyTypePositives 
                    if MaleBodyHeightPositives != "":
                        MaleTypeHeightFinal = MaleTypeHeightFinal + ", " + MaleBodyHeightPositives

                    if MaleAgePositives != "":
                        MaleAgeSkinFinal    = MaleAgeSkinFinal    + ", " + MaleAgePositives    
                    if MaleSkinPositives != "":
                        MaleAgeSkinFinal    = MaleAgeSkinFinal    + ", " + MaleSkinPositives 

                    if MaleWardrobePositives != "":
                        MaleWardrobeFinal   = MaleWardrobeFinal   + ", " + MaleWardrobePositives
                    if MaleWardrobeSubPositives != "":
                        MaleWardrobeFinal   = MaleWardrobeFinal   + ", " + MaleWardrobeSubPositives

                    if MaleFootwearPositives != "":
                        MaleFootwearFinal   = MaleFootwearFinal   + ", " + MaleFootwearPositives 
                    if MaleFootwearSubPositives != "":
                        MaleFootwearFinal   = MaleFootwearFinal   + ", " + MaleFootwearSubPositives

                    #3 TAB(Head)
                    if MaleFaceShapePositives != "":
                        MaleShapeExpressionFinal  = MaleShapeExpressionFinal    + ", " + MaleFaceShapePositives 
                    if MaleFaceExpressionPositives != "":
                        MaleShapeExpressionFinal  = MaleShapeExpressionFinal    + ", " + MaleFaceExpressionPositives

                    if MaleHairColorPositives != "":
                        MaleHairFinal             = MaleHairFinal + ", " + MaleHairColorPositives  
                    if MaleHairCutPositives != "":
                        MaleHairFinal             = MaleHairFinal + ", " + MaleHairCutPositives

                    if  MaleEyeShapePositives != "":
                        MaleEyesFinal             = MaleEyesFinal + ", " + MaleEyeShapePositives
                    if MaleEyeColorPositives != "":
                        MaleEyesFinal             = MaleEyesFinal + ", " + MaleEyeColorPositives

                    if MaleEyeBrowsPositives != "":
                        MaleBrowsGlassesFinal     = MaleBrowsGlassesFinal + ", " + MaleEyeBrowsPositives  
                    if MaleGlassesPositives != "":
                        MaleBrowsGlassesFinal     = MaleBrowsGlassesFinal + ", " + MaleGlassesPositives 
            
                    if MaleNosePositives != "":
                        MaleNoseChinFinal         = MaleNoseChinFinal + ", " + MaleNosePositives 
                    if MaleChinPositives != "":
                        MaleNoseChinFinal         = MaleNoseChinFinal + ", " + MaleChinPositives

                    if MaleMustachePositives != "":
                        MaleMustacheBeardFinal    = MaleMustacheBeardFinal + ", " + MaleMustachePositives   
                    if MaleBeardPositives != "":
                        MaleMustacheBeardFinal    = MaleMustacheBeardFinal + ", " + MaleBeardPositives 

                    if MaleHeadWearPositives != "":
                        MaleHeadWearFinal        = MaleHeadWearFinal + ", " + MaleHeadWearPositives
                    if MaleNecklessPositives != "":
                        MaleHeadWearFinal        = MaleHeadWearFinal + ", " + MaleNecklessPositives

                    if MaleQuickBackGroundPositives != "":
                        MaleQuickBackGroundResult = MaleQuickBackGroundResult + ", " + MaleQuickBackGroundPositives  

                    #3 TAB(RPG)
                    if MaleBodyArmorPositives != "" :
                        MaleBodyArmorResult    = MaleBodyArmorResult + ", "   + MaleBodyArmorPositives

                    if MaleHeadArmorPositives != "" :
                        MaleHeadNeckFinal      = MaleHeadNeckFinal + ", " + MaleHeadArmorPositives  
                    if MaleNeckArmorPositives != "" :
                        MaleHeadNeckFinal  = MaleHeadNeckFinal + ", " + MaleNeckArmorPositives

                    if MaleShoulderArmorPositives != "" :
                        MaleShoulderChestFinal = MaleShoulderChestFinal + ", " + MaleShoulderArmorPositives 
                    if MaleNeckArmorPositives != "" :
                        MaleShoulderChestFinal = MaleShoulderChestFinal + ", " + MaleNeckArmorPositives

                    if MaleLegArmorPositives != "" :
                        MaleLegGroinFinal      = MaleLegGroinFinal + ", " + MaleLegArmorPositives 
                    if MaleGroinArmorPositives != "":
                          MaleLegGroinFinal    = MaleLegGroinFinal + ", " + MaleGroinArmorPositives

                    if MaleWeaponPositives != "" :
                        MaleWeaponsFinal       = MaleWeaponsFinal + ", " + MaleWeaponPositives 
                    if MaleWeaponSubPositives != "" :
                        MaleWeaponsFinal       = MaleWeaponsFinal + ", " + MaleWeaponSubPositives

                    if MaleShieldPositives !=  "" :
                        MaleShieldFinal        = MaleShieldFinal + ", "  + MaleShieldPositives  


                # IF a dropdown menu has values add it to our main prompts 
                # More important values are added first (Medium , Type , God ,Embedding, Lora , Content Rating...)
                if MediumFinal != "":
                    MainPositive = MainPositive + ", " + MediumFinal 
                
                if FemaleTypeFinal != "":
                    MainPositive = MainPositive + ", " + FemaleTypeFinal

                if GoddessFinal != "":
                    MainPositive = MainPositive + ", " + GoddessFinal  
                
                if MaleGodFinal != "":
                    MainPositive = MainPositive + ", " + MaleGodFinal

                if CelebrityEmbeddingFinal != "":
                    MainPositive = MainPositive + ", " + CelebrityEmbeddingFinal

                if LoraResult != "":
                    MainPositive = MainPositive + ", " + LoraResult

                if ContentRatingResult != "":
                    MainPositive = MainPositive + ", " + ContentRatingResult

                if MaleTypeFinal !="":
                    MainPositive = MainPositive + ", " + MaleTypeFinal

                if MaleEmbeddingResult !="":
                    MainPositive = MainPositive + ", " + MaleEmbeddingResult

                if MaleLoraResult !="":
                    MainPositive = MainPositive + ", " + MaleLoraResult

                if MaleContentRatingResult !="":
                    MainPositive = MainPositive + ", " + MaleContentRatingResult 

                # After those values we add our user prompt if it exists 
                MainPositive += ", " + TempText 

                # Then we add less important values 

                if FinalResultColor != "":
                    MainPositive = MainPositive + ", " + FinalResultColor               
                
                if StyleLoraResult != "":
                    MainPositive = MainPositive + ", " + StyleLoraResult

                if StyleEmbeddingResult != "":
                    MainPositive = MainPositive + ", " + StyleEmbeddingResult 

                if StyleFinal != "":
                    MainPositive = MainPositive + ", " + StyleFinal
                
                if StyleGeneralResult != "":
                    MainPositive = MainPositive + ", " + StyleGeneralResult

                if MaterialFinal != "":
                    MainPositive = MainPositive + ", " + MaterialFinal

                if SeasonHolidayFinal != "":
                    MainPositive = MainPositive + ", " + SeasonHolidayFinal

                if LightingFinal != "":
                    MainPositive = MainPositive + ", " + LightingFinal
                
                if LightingEffectResult != "":
                    MainPositive = MainPositive + ", " + LightingEffectResult

                if ArtistsFinal != "":
                    MainPositive = MainPositive + ", " + ArtistsFinal
                
                if CameraResult1 != "":
                    MainPositive = MainPositive + ", " + CameraResult1

                if CameraResult2 != "":
                    MainPositive = MainPositive + ", " + CameraResult2

                if CameraResult3 != "":
                    MainPositive = MainPositive + ", " + CameraResult3

                if PhotographyFinal != "": 
                    MainPositive = MainPositive + ", " + PhotographyFinal

                # General

                if OriginColorFinal != "":
                    MainPositive = MainPositive + ", " + OriginColorFinal
                               
                if AgeResult != "":
                    MainPositive = MainPositive + ", " + AgeResult                         
                                    
                if BodyAngleFinal != "":
                    MainPositive = MainPositive + ", " + BodyAngleFinal

                if CameraLookingFinal != "":
                    MainPositive = MainPositive + ", " + CameraLookingFinal

                # Head 
                if ShapeExpressionFinal !="":
                    MainPositive = MainPositive + ", " + ShapeExpressionFinal

                if ColorCutFinal != "":
                    MainPositive = MainPositive + ", " + ColorCutFinal

                if EyeFinal !="":
                    MainPositive = MainPositive + ", " + EyeFinal

                if BrowsNoseFinal !="":
                    MainPositive = MainPositive + ", " + BrowsNoseFinal

                if LipChinFinal !="":
                    MainPositive = MainPositive + ", " + LipChinFinal

                # Head Accessories
                if HairEarsFinal !="":
                    MainPositive = MainPositive + ", " + HairEarsFinal

                if EarringsNecklessFinal !="":
                    MainPositive = MainPositive + ", " + EarringsNecklessFinal               

                if HatGlassesFinal !="":
                    MainPositive = MainPositive + ", " + HatGlassesFinal 

                # Body 
                if BodyTypeFinal !="":
                    MainPositive = MainPositive + ", " + BodyTypeFinal
                
                if SkinResult !="":
                    MainPositive = MainPositive + ", " + SkinResult
                
                if BreastFinal !="":
                    MainPositive = MainPositive + ", " + BreastFinal

                if AssFinal !="":
                    MainPositive = MainPositive + ", " + AssFinal

                if HipsLegsFinal !="":
                    MainPositive = MainPositive + ", " + HipsLegsFinal
                
                if WardrobeFinal !="":
                    MainPositive = MainPositive + ", " + WardrobeFinal
                
                if FootwearFinal !="":
                    MainPositive = MainPositive + ", " + FootwearFinal
                
                if QuickBackGroundResult !="":
                    MainPositive = MainPositive + ", " + QuickBackGroundResult

                # Female RPG
                if FemaleBodyArmorResult !="":
                    MainPositive = MainPositive + ", " + FemaleBodyArmorResult

                if FemaleHeadNeckFinal !="":
                    MainPositive = MainPositive + ", " + FemaleHeadNeckFinal

                if FemaleShoulderChestFinal !="":
                    MainPositive = MainPositive + ", " + FemaleShoulderChestFinal

                if FemaleLegGroinFinal !="":
                    MainPositive = MainPositive + ", " + FemaleLegGroinFinal
                
                if FemaleWeaponsFinal !="":
                    MainPositive = MainPositive + ", " + FemaleWeaponsFinal

                if FemaleShieldFinal !="":
                    MainPositive = MainPositive + ", " + FemaleShieldFinal

                # Male Character

                if MaleOriginColorFinal !="":
                    MainPositive = MainPositive + ", " + MaleOriginColorFinal

                if MaleViewAngleFinal !="":
                    MainPositive = MainPositive + ", " + MaleViewAngleFinal

                if MaleLookingFocusFinal !="":
                    MainPositive = MainPositive + ", " + MaleLookingFocusFinal

                if MaleTypeHeightFinal !="":
                    MainPositive = MainPositive + ", " + MaleTypeHeightFinal

                if MaleAgeSkinFinal !="":
                    MainPositive = MainPositive + ", " + MaleAgeSkinFinal

                if MaleWardrobeFinal !="":
                    MainPositive = MainPositive + ", " + MaleWardrobeFinal

                if MaleFootwearFinal !="":
                    MainPositive = MainPositive + ", " + MaleFootwearFinal

                # Male Head
                if MaleShapeExpressionFinal !="":
                    MainPositive = MainPositive + ", " + MaleShapeExpressionFinal

                if MaleHairFinal !="":
                    MainPositive = MainPositive + ", " + MaleHairFinal

                if MaleEyesFinal !="":
                    MainPositive = MainPositive + ", " + MaleEyesFinal
 
                if MaleBrowsGlassesFinal !="":
                    MainPositive = MainPositive + ", " + MaleBrowsGlassesFinal

                if MaleNoseChinFinal !="":
                    MainPositive = MainPositive + ", " + MaleNoseChinFinal

                if MaleMustacheBeardFinal !="":
                    MainPositive = MainPositive + ", " + MaleMustacheBeardFinal

                if MaleHeadWearFinal !="":
                    MainPositive = MainPositive + ", " + MaleHeadWearFinal

                if MaleQuickBackGroundResult !="":
                    MainPositive = MainPositive + ", " + MaleQuickBackGroundResult 

                # Male RPG
                if MaleBodyArmorResult !="":
                    MainPositive = MainPositive + ", " + MaleBodyArmorResult

                if MaleHeadNeckFinal !="":
                    MainPositive = MainPositive + ", " + MaleHeadNeckFinal

                if MaleShoulderChestFinal !="":
                    MainPositive = MainPositive + ", " + MaleShoulderChestFinal

                if MaleLegGroinFinal !="":
                    MainPositive = MainPositive + ", " + MaleLegGroinFinal
                
                if MaleWeaponsFinal !="":
                    MainPositive = MainPositive + ", " + MaleWeaponsFinal

                if MaleShieldFinal !="":
                    MainPositive = MainPositive + ", " + MaleShieldFinal

                if BeautifiersResult != "":
                    MainPositive = MainPositive + ", " + BeautifiersResult

                if BeautyDescResult != "":
                    MainPositive = MainPositive + ", " + BeautyDescResult 

                if MaleRatingDescFinal != "":
                    MainPositive = MainPositive + ", " + MaleRatingDescFinal

                if BeautifiersDetailsFinal != "":
                    MainPositive = MainPositive + ", " + BeautifiersDetailsFinal


                # Formating ',' if there are extras 
                MainPositive = MainPositive.replace(",,", ",")
                

                # User typed negative prompt
                MainNegative = p.negative_prompt
                

                # IF cbox for negatives is checked add all negatives into our MainNegative 
                if cbNegatives == True:
                                        
                    if NegativeEmbeddings != "":
                        MainNegative = NegativeEmbeddings 

                    MainNegative = " " + p.negative_prompt + ", " 

                    if ContentRatingResult != "" and ContentRatingNegatives != "" :
                        MainNegative = MainNegative  + ContentRatingNegatives 
                    if ContentRatingResult != "" and BeautyDescriptorNegatives != "":
                        MainNegative = MainNegative  + "," + BeautyDescriptorNegatives 
                    
                    if MaleRatingDescFinal != "" and MaleBodyTypeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleBodyTypeNegatives 
                    if MaleRatingDescFinal != "" and MaleContentRatingNegatives != "" :
                        MainNegative = MainNegative + MaleContentRatingNegatives

                    if MediumFinal         != "" and MediumNegatives !="":
                        MainNegative = MainNegative + "," + MediumNegatives
                    if MediumFinal         != "" and MediumSubNegatives != "" :
                        MainNegative = MainNegative + "," + MediumSubNegatives

                    if FinalResultColor != "" and ColorSchemeNegatives != "":
                        MainNegative = MainNegative + "," + ColorSchemeNegatives
                    if FinalResultColor != "" and ColorToneNegatives != "":
                        MainNegative = MainNegative + "," + ColorToneNegatives

                    if BeautifiersResult != "" and BeautifiersNegatives != "":
                        MainNegative = MainNegative + "," + BeautifiersNegatives  
                    if BeautifiersDetailsFinal != "" and DetailsNegatives != "":
                        MainNegative = MainNegative + "," + DetailsNegatives

                    if StyleLoraResult != "" and StyleLoraNegatives != "" :
                        MainNegative = MainNegative + "," + StyleLoraNegatives

                    if StyleEmbeddingResult != "" and StyleEmbeddingNegatives != "":
                        MainNegative = MainNegative + "," + StyleEmbeddingNegatives


                    if StyleFinal != "" and StyleGeneralNegatives != "":
                        MainNegative = MainNegative + "," + StyleGeneralNegatives
                    if StyleGeneralResult != "" and StyleGameNegatives != "":
                        MainNegative = MainNegative + "," + StyleGameNegatives

                    if MaterialFinal != "" and MaterialNegatives != "" :
                        MainNegative = MainNegative + "," + MaterialNegatives
                    if MaterialFinal != "" and MaterialSubNegatives != "":
                        MainNegative = MainNegative + "," + MaterialSubNegatives

                    if SeasonHolidayFinal != "" and SeasonNegatives != "" :
                        MainNegative = MainNegative + "," + SeasonNegatives 
                    if SeasonHolidayFinal != "" and HolidayNegatives != "":
                        MainNegative = MainNegative + "," + HolidayNegatives 

                    if LightingFinal != "" and LightingNegatives !="" :
                        MainNegative = MainNegative + "," + LightingNegatives
                    if LightingFinal != "" and LightingSubNegatives !="":
                        MainNegative = MainNegative + "," + LightingSubNegatives    
                    
                    if LightingEffectResult != "" and LightingEffectNegatives != "" :
                        MainNegative = MainNegative + "," + LightingEffectNegatives
                    
                    if ArtistsFinal     != "" and SingleArtistNegatives != "":
                        MainNegative = MainNegative + "," + SingleArtistNegatives
                    if ArtistsFinal     != "" and ArtistThemeNegatives != "":
                        MainNegative = MainNegative + "," + ArtistThemeNegatives

                    if CameraResult1    != "" and CameraShotTypeNegatives != "" :
                        MainNegative = MainNegative + "," + CameraShotTypeNegatives
                    if CameraResult1    != "" and CameraShotAngleNegatives != "" :
                        MainNegative = MainNegative + "," + CameraShotAngleNegatives

                    if CameraResult2    != "" and CameraFilmSizeNegatives != "" :
                        MainNegative = MainNegative + "," + CameraFilmSizeNegatives 
                    if CameraResult2    != "" and CameraBrandNegatives != "" :
                        MainNegative = MainNegative + "," + CameraBrandNegatives

                    if CameraResult3    != "" and CameraFocalLenNegatives != "" :
                        MainNegative = MainNegative + "," + CameraFocalLenNegatives
                    if CameraResult3    != "" and CameraFocusNegatives != "" :
                        MainNegative = MainNegative + "," + CameraFocusNegatives 

                    if PhotographyFinal != "" and PhotographyTypeNegatives != "":
                        MainNegative = MainNegative + "," + PhotographyTypeNegatives
                    if PhotographyFinal != "" and PhotographersNegatives != "":
                        MainNegative = MainNegative + "," + PhotographersNegatives

                    # General


                    if FemaleTypeFinal != "" and FemaleTypeNegatives != "" :
                        MainNegative = MainNegative + "," + FemaleTypeNegatives 
                    if FemaleTypeFinal != "" and SpecificPersonNegatives != "":
                        MainNegative = MainNegative + "," + SpecificPersonNegatives

                    if GoddessFinal != "" and GoddessTypeNegatives != "" :
                        MainNegative = MainNegative + "," + GoddessTypeNegatives
                    if GoddessFinal != "" and GoddessNegatives != "":
                        MainNegative = MainNegative + "," + GoddessNegatives

                    if CelebrityEmbeddingFinal != "" or EmbeddingNegatives != "":
                        MainNegative = MainNegative + "," + EmbeddingNegatives
                    
                    if LoraResult != "" or LoraNegatives !="":
                        MainNegative = MainNegative + "," + LoraNegatives 

                    if OriginColorFinal != "" and OriginOrNationalityNegatives != "" :
                        MainNegative = MainNegative + "," + OriginOrNationalityNegatives
                    if OriginColorFinal != "" and SkinColorNegatives != "":
                        MainNegative = MainNegative + "," + SkinColorNegatives 

                    if AgeResult != "" and AgeNegatives != "" :
                        MainNegative = MainNegative + "," + AgeNegatives                       
                                        
                    if BodyAngleFinal != "" and BodyViewNegatives != "" :
                        MainNegative = MainNegative + "," + BodyViewNegatives
                    if BodyAngleFinal != "" and CameraAngleNegatives != "" :
                        MainNegative = MainNegative + "," + CameraAngleNegatives

                    if CameraLookingFinal != "" and CameraFocusNegatives != ""  :
                        MainNegative = MainNegative + "," + CameraFocusNegatives
                    if CameraLookingFinal != "" and LookingWhereNegatives != "" :
                        MainNegative = MainNegative + "," + LookingWhereNegatives

                    # Head 
                    if ShapeExpressionFinal != "" and FaceExpressionNegatives != "":
                        MainNegative = MainNegative + "," + FaceExpressionNegatives 
                    if ShapeExpressionFinal != "" and FaceShapeNegatives != "" :
                        MainNegative = MainNegative + "," + FaceShapeNegatives

                    if ColorCutFinal != "" and HairColorNegatives != "" :
                        MainNegative = MainNegative + "," + HairColorNegatives 
                    if ColorCutFinal != "" and HairCutNegatives != "" :
                        MainNegative = MainNegative + "," + HairCutNegatives

                    if EyeFinal !="" and EyeColorNegatives != "" :
                        MainNegative = MainNegative + "," + EyeColorNegatives
                    if EyeFinal !="" and EyeShapeNegatives != "" :
                        MainNegative = MainNegative + "," + EyeShapeNegatives

                    if BrowsNoseFinal !="" and EyeBrowsNegatives != "" :
                        MainNegative = MainNegative + "," + EyeBrowsNegatives  
                    if BrowsNoseFinal !="" and NoseNegatives != "" :
                        MainNegative = MainNegative + "," + NoseNegatives 

                    if LipChinFinal !="" and LipNegatives != "" :
                        MainNegative = MainNegative + "," + LipNegatives 
                    if LipChinFinal !="" and ChinNegatives != "" :
                        MainNegative = MainNegative + "," + ChinNegatives 

                    # Head Accessories
                    if HairEarsFinal !="" and HairAccessoryNegatives != "" :
                        MainNegative = MainNegative + "," + HairAccessoryNegatives 
                    if HairEarsFinal !="" and AnimalEarsNegatives != ""  :
                        MainNegative = MainNegative + "," + AnimalEarsNegatives 

                    if EarringsNecklessFinal !="" and EarringsNegatives != "":
                        MainNegative = MainNegative + "," + EarringsNegatives  
                    if EarringsNecklessFinal !="" and NecklessNegatives != "" :
                        MainNegative = MainNegative + "," + NecklessNegatives

                    if HatGlassesFinal !="" and HatNegatives != "" :
                        MainNegative = MainNegative + "," + GlassesNegatives
                    if HatGlassesFinal !="" and GlassesNegatives != "" :
                        MainNegative = MainNegative + "," + HatNegatives 

                    # Body 
                    if BodyTypeFinal !="" and BodyTypeNegatives != "" :
                        MainNegative = MainNegative + "," + BodyTypeNegatives 
                    
                    if BreastFinal !="" and BreastSizeNegatives != "" :
                        MainNegative = MainNegative + "," + BreastSizeNegatives 
                    if BreastFinal !="" and  BreastDescriptorNegatives != "" :
                        MainNegative = MainNegative + "," + BreastDescriptorNegatives

                    if AssFinal !="" and AssSizeNegatives != "":
                        MainNegative = MainNegative + "," + AssSizeNegatives 
                    if AssFinal !="" and AssDescriptorNegatives != "" :
                        MainNegative = MainNegative + "," + AssDescriptorNegatives

                    if HipsLegsFinal !="" and HipsNegatives != "":
                        MainNegative = MainNegative + "," + HipsNegatives 
                    if HipsLegsFinal !="" and LegsDescriptorNegatives != "" :
                        MainNegative = MainNegative + "," + LegsDescriptorNegatives

                    if WardrobeFinal !="" and WardrobeNegatives != "" :
                        MainNegative = MainNegative + "," + WardrobeNegatives 
                    if WardrobeFinal !="" and WardrobeSubNegatives != "" :
                        MainNegative = MainNegative + "," + WardrobeSubNegatives

                    if FootwearFinal !="" and FootwearNegatives != ""  :
                        MainNegative = MainNegative + "," + FootwearNegatives
                    if FootwearFinal !="" and FootwearSubNegatives != "" :
                        MainNegative = MainNegative + "," + FootwearSubNegatives 

                    if QuickBackGroundResult !="" and QuickBackGroundNegatives != "":
                        MainNegative = MainNegative + "," + QuickBackGroundNegatives


                    # Female RPG
                    if FemaleBodyArmorResult !="" and FemaleBodyArmorNegatives != "":
                        MainNegative = MainNegative + "," + FemaleBodyArmorNegatives

                    if FemaleHeadNeckFinal !="" and FemaleHeadArmorNegatives != "" :
                        MainNegative = MainNegative + "," +  FemaleHeadArmorNegatives
                    if FemaleHeadNeckFinal !="" and FemaleNeckArmorNegatives != "" :
                        MainNegative = MainNegative + "," +  FemaleNeckArmorNegatives

                    if FemaleShoulderChestFinal !="" and FemaleShoulderArmorNegatives !="" :
                        MainNegative = MainNegative + "," + FemaleShoulderArmorNegatives
                    if FemaleShoulderChestFinal !="" and FemaleChestArmorNegatives !="":
                        MainNegative = MainNegative + "," + FemaleChestArmorNegatives

                    if FemaleLegGroinFinal !="" and FemaleLegArmorNegatives !="" :
                        MainNegative = MainNegative + "," +  FemaleLegArmorNegatives 
                    if FemaleLegGroinFinal !="" and FemaleGroinArmorNegatives !="" :
                        MainNegative = MainNegative + "," +  FemaleGroinArmorNegatives

                    if FemaleWeaponsFinal != "" and FemaleWeaponNegatives != "":
                        MainNegative = MainNegative + "," + FemaleWeaponNegatives 
                    if FemaleWeaponsFinal != "" and FemaleWeaponSubNegatives !="":
                        MainNegative = MainNegative + "," +  FemaleWeaponSubNegatives

                    if FemaleShieldFinal !="" and FemaleShieldNegatives !="" :
                        MainNegative = MainNegative + "," + FemaleShieldNegatives


                    # Male Character

                    if MaleTypeFinal !="" and MaleTypeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleTypeNegatives

                    if MaleGodFinal != "" and MaleGodTypeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleGodTypeNegatives
                    if MaleGodFinal != "" and MaleGodNegatives != "":
                        MainNegative = MainNegative + "," + MaleGodNegatives

                    if MaleEmbeddingResult !="" and MaleEmbeddingNegatives != "" :
                        MainNegative = MainNegative + "," + MaleEmbeddingNegatives

                    if MaleLoraResult !="" and MaleLoraNegatives != "" :
                        MainNegative = MainNegative + "," + MaleLoraNegatives 

                    if MaleOriginColorFinal !="" and MaleOriginOrNationalityNegatives != "" :
                        MainNegative = MainNegative + "," + MaleOriginOrNationalityNegatives 
                    if MaleOriginColorFinal !="" and MaleSkinColorNegatives !=  "" :
                        MainNegative = MainNegative + "," + MaleSkinColorNegatives

                    if MaleViewAngleFinal !="" and MaleBodyViewNegatives != "": 
                        MainNegative = MainNegative + "," + MaleBodyViewNegatives 
                    if MaleViewAngleFinal !="" and MaleBodyAngleNegatives != "" : 
                        MainNegative = MainNegative + "," + MaleBodyAngleNegatives

                    if MaleLookingFocusFinal !="" and MaleLookingWhereNegatives != "" :
                        MainNegative = MainNegative + "," + MaleLookingWhereNegatives
                    if MaleLookingFocusFinal !="" and MaleBodyFocusNegatives !=  "" :
                        MainNegative = MainNegative + "," +  MaleBodyFocusNegatives

                    if MaleTypeHeightFinal !="" and MaleBodyTypeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleBodyTypeNegatives 
                    if MaleTypeHeightFinal !="" and MaleBodyHeightNegatives !=  "" :
                        MainNegative = MainNegative + "," + MaleBodyHeightNegatives

                    if MaleAgeSkinFinal !="" and MaleAgeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleAgeNegatives 
                    if MaleAgeSkinFinal !="" and MaleSkinNegatives !=  ""  :
                        MainNegative = MainNegative + "," + MaleSkinNegatives

                    if MaleWardrobeFinal !="" and MaleWardrobeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleWardrobeNegatives 
                    if MaleWardrobeFinal !="" and MaleWardrobeSubNegatives != "" :
                        MainNegative = MainNegative + "," + MaleWardrobeSubNegatives

                    if MaleFootwearFinal !="" and MaleFootwearNegatives != "" :
                        MainNegative = MainNegative + "," + MaleFootwearNegatives 
                    if MaleFootwearFinal !="" and  MaleFootwearSubNegatives != "" :
                        MainNegative = MainNegative + "," + MaleFootwearSubNegatives

                    # Male Head
                    if MaleShapeExpressionFinal !="" and MaleFaceShapeNegatives != ""  :
                        MainNegative = MainNegative + "," + MaleFaceShapeNegatives
                    if MaleShapeExpressionFinal !="" and MaleFaceExpressionNegatives !=  "" :
                        MainNegative = MainNegative + "," + MaleFaceExpressionNegatives

                    if MaleHairFinal !="" and MaleHairCutNegatives != "" :
                        MainNegative = MainNegative + "," + MaleHairCutNegatives 
                    if MaleHairFinal !="" and MaleHairColorNegatives != ""  :
                        MainNegative = MainNegative + "," + MaleHairColorNegatives

                    if MaleEyesFinal != "" and MaleEyeShapeNegatives != "" :
                        MainNegative = MainNegative + "," + MaleEyeShapeNegatives
                    if MaleEyesFinal != "" and  MaleEyeColorNegatives != "":
                        MainNegative = MainNegative + "," + MaleEyeColorNegatives

                        
                    if MaleBrowsGlassesFinal !="" and MaleEyeBrowsNegatives != "":
                        MainNegative = MainNegative + "," + MaleEyeBrowsNegatives  
                    if MaleBrowsGlassesFinal !="" and MaleGlassesNegatives !=  "" :
                        MainNegative = MainNegative + "," + MaleGlassesNegatives

                    if MaleNoseChinFinal !="" and MaleNoseNegatives != ""  :
                        MainNegative = MainNegative + "," + MaleNoseNegatives 
                    if MaleNoseChinFinal !="" and MaleChinNegatives !=  "" :
                        MainNegative = MainNegative + "," + MaleChinNegatives

                    if MaleMustacheBeardFinal !=""  and MaleBeardNegatives != "":
                        MainNegative = MainNegative + "," + MaleBeardNegatives 
                    if MaleMustacheBeardFinal !=""  and MaleMustacheNegatives !=  "":
                        MainNegative = MainNegative + "," +  MaleMustacheNegatives

                    if MaleHeadWearFinal !="" and MaleHeadWearNegatives != "" :
                        MainNegative = MainNegative + "," + MaleBeardNegatives 
                    if MaleHeadWearFinal !="" and  MaleNecklessNegatives !=  "":
                        MainNegative = MainNegative + "," + MaleNecklessNegatives

                    if MaleQuickBackGroundResult != "" and MaleQuickBackGroundNegatives != "" :
                        MainNegative = MainNegative + "," + MaleQuickBackGroundNegatives                  

                    # Male RPG
                    if MaleBodyArmorResult !="" and MaleBodyArmorNegatives != "":
                        MainNegative = MainNegative + "," + MaleBodyArmorNegatives

                    if MaleHeadNeckFinal !="" and MaleHeadArmorNegatives !="" :
                        MainNegative = MainNegative + "," +  MaleHeadArmorNegatives  
                    if MaleHeadNeckFinal !="" and MaleNeckArmorNegatives != "" :
                        MainNegative = MainNegative + "," +  MaleNeckArmorNegatives

                    if MaleShoulderChestFinal !="" and MaleShoulderArmorNegatives !="" :
                        MainNegative = MainNegative + "," + MaleShoulderArmorNegatives 
                    if MaleShoulderChestFinal !="" and MaleChestArmorNegatives !="" :
                        MainNegative = MainNegative + "," + MaleChestArmorNegatives

                    if MaleLegGroinFinal !="" and MaleLegArmorNegatives !="" :
                        MainNegative = MainNegative + "," + MaleLegArmorNegatives 
                    if MaleLegGroinFinal !="" and MaleGroinArmorNegatives !="" :
                        MainNegative = MainNegative + "," + MaleGroinArmorNegatives

                    if MaleWeaponsFinal != "" and MaleWeaponNegatives != "":
                        MainNegative = MainNegative + "," + MaleWeaponNegatives 
                    if MaleWeaponsFinal != "" and  MaleWeaponSubNegatives !="":
                        MainNegative = MainNegative + "," + MaleWeaponSubNegatives

                    if MaleShieldFinal !="" and MaleShieldNegatives !="" :
                        MainNegative = MainNegative + "," + MaleShieldNegatives

                    if NegativeTagsFinal != "" :
                        MainNegative += "".join(NegativeTagsFinal)
                 
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


