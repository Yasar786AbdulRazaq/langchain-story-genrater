
!pip install -q -U google-generativeai


# Import the Python SDK
import google.generativeai as genai
# Used to securely store your API key
from google.colab import userdata

GOOGLE_API_KEY=userdata.get('GOOGLE_API_KEY')
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel('gemini-1.5-flash-latest')



response = model.generate_content("write a story on a mounky data.")
print(response.text)

The air hung thick and humid, the scent of overripe mangoes clinging to the humid air.  Deep within the emerald heart of the Amazon, nestled amongst the whispering lianas and the chattering howler monkeys, lived a peculiar creature: Miko, a monkey… with a peculiar talent for data.

Miko wasn't like the other monkeys. While they swung effortlessly through the canopy, chasing insects and squabbling over the juiciest fruits, Miko spent his days meticulously organizing fallen leaves.  Not just any leaves, mind you. These were special leaves, each marked with a unique pattern of veins, a tiny, natural barcode.

He'd collected thousands, categorizing them by shape, size, and the specific type of tree they'd fallen from. He'd even developed a system of notches carved into a particularly sturdy branch, a rudimentary counting system that allowed him to track the number of each leaf type.  He’d observed, for instance, that the number of serrated leaves from the Kapok tree correlated with rainfall. More rain, more leaves.  It was his own little, incredibly detailed, arboreal dataset.

One day, a group of scientists arrived, their brightly coloured clothes a stark contrast to the muted greens and browns of the jungle. They were studying the effects of deforestation on the rainforest ecosystem. They were brilliant, armed with sophisticated equipment, but they lacked the granular, intimate knowledge of the forest that Miko possessed.

Initially, they dismissed Miko as just another monkey, a curious observer of their activity.  But one day, while observing their data collection efforts – tedious measurements and complicated algorithms – Miko approached them, offering a carefully selected pile of his leaves.  The scientists were baffled.

Dr. Anya Sharma, the lead researcher, noticed the intricate system of notches and the remarkably consistent patterns in the leaf collection.  After painstaking hours, translating Miko's leaf-based system, she realized the depth of his observation. Miko’s data, collected over years, revealed subtle shifts in the forest's health – shifts far earlier than their own sophisticated instruments could detect.

His meticulously recorded leaf data provided early warnings of impending ecological changes, insights into the delicate balance of the rainforest far more accurate than any model they had developed. Miko’s unique dataset, born from simple observation and remarkable dedication, became invaluable to their research.

The scientists worked with Miko, developing a better communication system – a series of whistles and gestures – that allowed them to understand his data more quickly.  His leaf-based system became an integral part of their models, predicting future changes with unprecedented accuracy.

Miko, the data monkey, became a legend.  He showed the world that even the simplest observer, with a deep understanding and unwavering dedication, could contribute to groundbreaking scientific discovery. The jungle, once merely his home, was now his laboratory, his data continuing to protect its delicate balance for years to come.
