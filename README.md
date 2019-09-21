# YTAPI

YTAPI (YouTube Transcribe API) for **[The Abuse Project](https://github.com/theabuseproject)** is a python API (Application Programming Interface) which allows you to get the transcript/subtitle for a given YouTube video in a nice list consisting of dictionaries. It also works for videos which have automatically generated subtitles. It does not use any _hacky mechanisms_.

## Install

For using this library in your project, simple use `pip` to install the module.

```
pip install ytapi
```

The module published is in it's early stage as of now, as it's being used internally in **The Abuse Project**. If you want to develop it further, you'll have to use this source repository.

```
git clone https://github.com/theabuseproject/YTAPI.git
```

After cloning, install the dependencies using pip,

```
pip install -r requirements.txt
```
## Usage

The implemented API class can be found under `ytapi/ytapi.py`.

```python
import ytapi
ytapi.YTAPI.get_transcript("Youtube Video ID")
```

#### Example Usage

```python
>>> import ytapi
>>> video = 'http://www.youtube.com/watch?v=BaW_jenozKc'
>>> video_id = video.split('?v=')[1]
>>> video_subtitles = ytapi.YTAPI.get_transcript(video_id)
>>> print(video_subtitles)
[{'text': 'This a test video\nfor youtube-dl', 'start': 0.26, 'duration': 3.33}, {'text': 'For more information\ncontact phihag@phihag.de', 'start': 3.59, 'duration': 6.08}]
>>>
>>> type(video_subtitles)
<class 'list'>
>>> type(video_subtitles[0])
<class 'dict'>
>>>
```