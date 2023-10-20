# open-ai-hmdb-data

To get your own API keys: https://platform.openai.com/account/api-keys <br />
Above is the link to if you want to specifically utilize OpenAI as the LLM, but other options exist like HuggingFace

**Short Explanation:**
I wrote this code while doing this internship under Dr. Leo at Boston's MGH and in particular we were investigating some NMR (Nuclear Magnetic Resonance https://en.wikipedia.org/wiki/Nuclear_magnetic_resonance) data from various experiments.  One thing that we wanted to be able to do was to give the program a certain ppm peak range (in my example I did from 1.00 to 1.03) and the program would respond by giving certain metabolites that match those peak ranges.  I took the data from the offical Human Metabolome Data Base (https://hmdb.ca/downloads), specifically, the .xml files.  I spent a lot of time writing a bunch of different file reader and reorganizer codes to eventually get the dataset ()

Even though this approach didn't yield particularly groundbreaking results, I at minimum learned a lot from the experience.  This was very new territory for me so I used a lot of online resources to basically teach myself everything.



**For OpenAI_With_HMDB_Data**

**Resulting Metabolites:**
7-Dehydrocholesterol, Aldosterone, Androstenedione, Glycocholic acid, L-Isoleucine, Testosterone, Propionic acid, 3b-Hydroxy-5-cholenoic acid, 16-a-Hydroxypregnenolone, 17-Hydroxyprogesterone, Etiocholanolone, 7-Ketocholesterol, Chenodeoxycholic acid, PC(16:0/16:0), Deoxycholic acid, Deoxycholic acid glycine conjugate, Cholesterol sulfate, Hyodeoxycholic acid, 3-Hexanone, Lithocholic acid, Stearic acid, beta-Sitosterol, Vitamin D3, L-Valine, Ergocalciferol, Tetrahydrocortisone, Stigmasterol, Ursodeoxycholic acid, Progesterone, all-trans-Retinoic acid, alpha-Tocopherol, Menthol, Azithromycin, Deoxycorticosterone, 17a-Hydroxypregnenolone, Epiandrosterone, 5alpha-And

