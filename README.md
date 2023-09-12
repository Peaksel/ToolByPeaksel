# ToolByPeaksel

**What is it?**

Tool by Peaksel is a prompt helper extension for Web UI. Built for beginners and professionals alike, it will enrich and speed up your workflow and improve the final quality of the resulting images.

Using random values will help you generate an unlimited number of prompts in one go, so it is perfect for composition hunting and prompt fin-tuning - the initial stage.

**How to install?**

You can install this extension by going to Extensions > Install from URL and pasting the GitHub link into the field, or by downloading and putting the folder manually to your SD root > Extensions folder.

https://github.com/Peaksel/ToolByPeaksel

To have all working out of the box, download and unzip negative embeddings and female character embeddings into your SD Root > Embeddings folder.

Negative Embeddings
https://app.box.com/s/mme8qwckkxf155nzv5h1wy291md53y53

Female characters embeddings
https://app.box.com/s/mmo5mnyp6eqmg15bcy3xyjswsn8i5sim

**How to use**

The “General” Tab should be used for all the images. “Female Character” or “Male Character” - should be used on top of “General” for character creation.

Use your positive and negative prompts as usual. Values you choose from the script will be added to the prompt.

**I. Tab: General**

“Beautifiers” and “Details” - chose manually or set to random

“Medium Type”: 6 main types with a lot of subtypes for you to explore.

“Negatives”. The “General” group of negative tags applies to all images, “b&w” prevents black and white images, and “character” prevents bad anatomy for character design. 

Choose “general+b&w” for non-character images and “general+character+b&w” for character images.

“Negative embeddings”. Download and extract the content of the file above to your SD install folder/embeddings for this to work. For general-purpose images choose two from the general-purpose section. If you are doing a character choose two from the “Hands Helpers” section. Use checkpoint specific only if using on the checkpoints it was intended for.

“Style Lora” and “Style Embedding” do not have working values. If you are using any for style, feel free to edit appropriate files in the variables folder.

“Style General” and “Style of Video Game”: Use one of these to define the style of the composition. Using both at the same time at random may produce surprising or bad results. Default strength is 

“Color Tone” and “Color scheme”: pick or randomize collar palettes and predefined color schemes.

“Artists” lets you choose one artist. “Artist Theme” lets you choose by art direction and backs it up with related artist names. Choose one of two if using random or combine fixed values.

“Material” will let you choose what is something made of and let you choose more precise values from sub-categories.

“Season” is obviously related to outdoor images or atmosphere.

“Exact Holiday” lets you pick a holiday recognized by SD. Works okay for interiors (decoration etc).

“Lighting” lets you pick a group of lighting based on darkness and also natural lights. All categories have a big choice. Recommended to use, adds an extra touch to your image.

“Lighting Effect” has a single effect choice. Choose the one you like or enjoy random results from here.

“Camera Shot Type” (example: medium shot), and “Camera Shot Angle” (example: shot from above) are related to scene composition. Not intended to use both at random as values may conflict. Choose fixed values.

“Camera Brand”, “Camera Film Size”, “Camera Focus” and “Camera Focal Length” are  more detailed camera settings with safe values set as favorites for non-photographers.

“Photography Type” lets you choose the photography type and for each type, you can enable a variety of related photographers in the “Photographers” sub-menu.

“Variables” are inherited from StylePile. Lets you use sequential, custom positive prompt values in X and Y fields (one per line). The number of these values will multiply your batch count or batch size values if different from 1. Using both A and B will produce: Batch Count x X x Y number of images.
Fields marked A, B, and C will use only one random value from the list you put in them.
To use a field, add [A] or any other field to your positive prompt.

**II. Tab: Female Character**

“Beauty Descriptor” offers single-word positive words related to female characters.

“Content Rating”: SWF (safe for work) is needed to prevent nudes (still may happen). NSFW (not safe for work) will do the opposite.

“Female Type”: A couple of standard values like “1girl” or “a woman” to get you started, the Female celebrity category is full of celebrities supported by Stable Diffusion without plugins. The Superhero category has a good list of female characters, but you may have better results with Marvel-themed plugins from this list.

“Embedding” and “Lora” are intended for exact female characters that require a plugin. For embeddings to work, download and extract this to your embeddings folder. Loras you can edit yourself as you see fit. If using plugins, you don’t have to define many values available below, only the ones you want different than in the embedding or Lora results.

“Origin or Nationality” is one way and “Skin Color” is another way. Use fixed values if using both or you will risk getting weird combinations.

“Body View” (example: upper body, portrait etc.) and “Camera Angle” (example: front view, back view, profile) will help you get your camera in place.

“Camera Focus” is also helpful. Breasts focus will help produce a front view, upper body image, face focus for close-up shots, and ass focus for a back view of the upper body.

“Looking Where” - the most used is looking at the viewer, but you may need other values as well.

“Body Type” and “Age” will help you define your character. “Skin” has skin decoration and skin details tags. Freckles and skin pores will help or force close-up shots.

“Breast Size” and “Breast Descriptor” are there for size and shape. They will force the front body view.

“Ass size” and “Ass Descriptor” are the same but will force back or side view if used.

“Hips” and “Legs Descriptor” will further help define the body shape.

“Wardrobe” features 21 categories of wardrobe with a lot of values in each sub-category.

“Footwear” features 9 categories with multiple values as well. Using it may force full-body view or a sitting position.

“Face Shape” does what it says.

“Face Expression” is there to help from the prompting side. Some values will work out of the box but for more complex ones you may want to use ControlNet with a reference image.

“Hair Color” and “Haircuts” will cover your hair problems. “Eye Color”, “Eye Shape”, “Eyebrows” “Nose”, “Lips” and “Chin” are all part of the face designing process.

As for the Head Accessories, you can choose one of “Hair Accessories” or “Animal Ears”. “Earrings”, “Neckless”, “Hat” and “Glasses” will help you further decorate the head area.

“Quick Background” is there if you don’t want SD to decide on it based on the other tags. Some style settings may impose a background if not defined but could be a good one. Optional use.

“RPG Dress up Corner” is a bonus section and should be used without “Wardrobe” or “Footwear” values from earlier. A variety of shields and armors are available from “Full Body Armor”, “Head Protection”, “Neck Protection”, “Shoulder Protection”, “Torso Protection” “Legs Protection” and “Groin Protection” categories. These are from the official Danbooru wiki but based on the checkpoints you use, the results may differ. Anime models should probably give better results.

“Weapons” will let choose from 8 weapons categories full of wiki-supported weapons. Again, limited results without ControlNet and reference image.

“Hand-held Shield” puts a shield on the arm.

**III Tab: Male Character**

Very similar usage to Female Character. As expected, some values are adjusted for a male character: “Male Type”, “Body Type” and the dress-up related tags. Additional categories are “Moustache” and “Beard”. 


**License**

Tool by Peaksel is a free software, released under [General Public License 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html).
It follows the same license as the [Style Pile](https://github.com/some9000/StylePile) script, which was used as an inspiration and starting code base for this project.

**Credits**

Script developed and released by [Peaksel](https://www.peaksel.com/ "Peaksel's Homepage"), a video games company based in Serbia ([LinkedIn](https://www.linkedin.com/company/peaksel-doo/ "Peaksel's LinkedIn")):

Marko Petkovic ([LinkedIn](https://www.linkedin.com/in/petkovicmarko/)): UI, data collection, and end-user testing

Andrija Ivkovic ([LinkedIn](https://www.linkedin.com/in/andrija-ivkovic-6a6285261/)): development, data collection, and functional testing

Dusan Ilic ([LinkedIn](https://www.linkedin.com/in/du%C5%A1an-ili%C4%87-a9a85173/)): development

Values for the script are obtained from multiple sources: [Danbooru](https://danbooru.donmai.us/), AI chatbots ([ChatGPT](https://chat.openai.com/), [Bard](https://bard.google.com/), [Bing](https://www.bing.com/search?q=bing+ai&form=ANNTH1&refig=2422a3eae03b42f5a8961a9afb6f42d8)), and [Civitai](https://civitai.com/?query=wildcards&view=feed) community.

**Support**

Please let us know about the bugs, feature requests, and new values to add. If you are a member, leave a comment on our [Civitai release page](https://civitai.com/models/99663/tool-by-peaksel-prompting-helper-script-stylepile-on-steroids) or send us an email to: office {at] peaksel {dot} email
