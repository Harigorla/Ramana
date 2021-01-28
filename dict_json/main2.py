import json

dict_ = {"20090209.02s1.1_sequence.txt": [645045714, 3559.6422951221466, 206045184], "20090209.02s1.2_sequence.txt": [645045714, 3543.8322949409485, 234618880]}
values = [{"file_name": k, "file_information": v} for k, v in dict_.items()]
json.dumps(values, indent=4)
