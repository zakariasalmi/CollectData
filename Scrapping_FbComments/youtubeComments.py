import pandas as pd

# Load the existing dataset
file_path = 'C:/Users/zakar/anaconda3/Untitled Folder 7/commentaires_normalises_final.csv'  # Update with your file path
df = pd.read_csv(file_path)

# Prepare new comments
new_comments = [
    {
        "user_name": "Fatima Zahra",
        "user_link": "https://www.facebook.com/fatima.zahra.123",
        "text": "خفت بزاف هاد المرة، الله يحفظنا جميعاً.",
        "timestamp": "Monday 11 September 2023 at 10:00",
        "likes_number": 15,
        "date": "11/9/2023",
        "time": "10:00"
    },
    {
        "user_name": "Ahmed El Khatib",
        "user_link": "https://www.facebook.com/ahmed.elkhatib.456",
        "text": "الزلزال كان قوي جداً، ما عرفتش شنو ندير.",
        "timestamp": "Monday 11 September 2023 at 10:05",
        "likes_number": 12,
        "date": "11/9/2023",
        "time": "10:05"
    },
    {
        "user_name": "Khadija Amrani",
        "user_link": "https://www.facebook.com/khadija.amrani.789",
        "text": "وليت ما كنقدرش ننعس من كثرة الخوف.",
        "timestamp": "Monday 11 September 2023 at 10:10",
        "likes_number": 20,
        "date": "11/9/2023",
        "time": "10:10"
    },
    {
        "user_name": "Youssef Benomar",
        "user_link": "https://www.facebook.com/youssef.benomar.012",
        "text": "كنت فالدّار، حسّيت بالأرض كتحرك تحتيا، خفت بزاف.",
        "timestamp": "Monday 11 September 2023 at 10:15",
        "likes_number": 25,
        "date": "11/9/2023",
        "time": "10:15"
    },
    {
        "user_name": "Mouna Ait El Cadi",
        "user_link": "https://www.facebook.com/mouna.aitelcadi.345",
        "text": "اللحظة لي حسّيت فيها بالزلزال، قلبي بغى يوقف.",
        "timestamp": "Monday 11 September 2023 at 10:20",
        "likes_number": 18,
        "date": "11/9/2023",
        "time": "10:20"
    },
    {
        "user_name": "Rachid Bouhali",
        "user_link": "https://www.facebook.com/rachid.bouhali.678",
        "text": "الله يحفظنا، هاد الشي بزاف علينا، خفنا بزاف.",
        "timestamp": "Monday 11 September 2023 at 10:25",
        "likes_number": 22,
        "date": "11/9/2023",
        "time": "10:25"
    },
    {
        "user_name": "Amina Lmoumni",
        "user_link": "https://www.facebook.com/amina.lmoumni.901",
        "text": "الزلزال كان مفاجئ وخلاني نحس بالرعب.",
        "timestamp": "Monday 11 September 2023 at 10:30",
        "likes_number": 19,
        "date": "11/9/2023",
        "time": "10:30"
    },
    {
        "user_name": "Mohamed El Amrani",
        "user_link": "https://www.facebook.com/mohamed.elamrani.234",
        "text": "هزّ الأرض بقوة، ما كنتش نتصور نشوف هاد النهار.",
        "timestamp": "Monday 11 September 2023 at 10:35",
        "likes_number": 30,
        "date": "11/9/2023",
        "time": "10:35"
    },
    {
        "user_name": "Sara El Ouafi",
        "user_link": "https://www.facebook.com/sara.elouafi.567",
        "text": "منين سمعنا الصوت ديال الزلزال، كلشي خرج يجري من الدار، رعب حقيقي.",
        "timestamp": "Monday 11 September 2023 at 10:40",
        "likes_number": 28,
        "date": "11/9/2023",
        "time": "10:40"
    },
    {
        "user_name": "Nabil El Khalfi",
        "user_link": "https://www.facebook.com/nabil.elkhalfi.890",
        "text": "خفت على ولادي وعلى راسي، الله يحفظ الجميع.",
        "timestamp": "Monday 11 September 2023 at 10:45",
        "likes_number": 35,
        "date": "11/9/2023",
        "time": "10:45"
    }
]

# Convert new comments to DataFrame
new_comments_df = pd.DataFrame(new_comments)

# Append new comments to the existing dataset
updated_df = pd.concat([df, new_comments_df], ignore_index=True)

# Save the updated dataset back to a CSV file
updated_file_path = '/mnt/data/updated_dataset.csv'  # Update with your desired file path
updated_df.to_csv(updated_file_path, index=False)

print(f"Updated dataset saved to {updated_file_path}")
