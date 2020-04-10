import csv
import json

chapters = []

with open('data/data.csv') as csvfile:
  reader = csv.DictReader(csvfile)
  for row in reader:
    serial = row['Serial']
    try:
      center = [float(row['Long_4dig']), float(row['Lat_4dig'])]
      story = row['Story']
      date = row['Date_Value']
      taluka = row['Taluka']
      if (story):
        this_chapter = {
          "id": "",
          "title": 'Title',
          "image": '',
          "description": 'Copy these sections to add to your story.',
          "location": {
            "center": [-77.020636, 38.886900],
            "zoom": 13.5,
            "pitch": 0,
            "bearing": 0
          },
          "onChapterEnter": [],
          "onChapterExit": []
        }
        this_chapter["id"] = serial
        this_chapter['title'] = taluka + ', ' + date
        this_chapter['description'] = story
        this_chapter['location']['center'] = center
        chapters.append(this_chapter)
    except:
      pass

print(json.dumps(chapters, indent=4))