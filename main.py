from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/faculties")
async def get_faculties():
    return ['фрекс']

@app.get("/specialties")
async def get_specialties(faculty: str):
    return ['кі', 'пф', 'рт']

@app.get("/courses")
async def get_courses():
    return ['1 бакалавр', '2 бакалавр', '3 бакалавр', '4 бакалавр', '1 магістр', '2 магістр']

@app.get("/groups")
async def get_groups(specialty: str, course: str):
    return ['птфе', 'нфне']

@app.get("/schedule")
async def get_schedule(date: str, faculty: str, specialty: str, course: str, group: str):
    if date == '12.11.2024':
        is_online = False
        lessons = [
            {
                'number': 1,
                'time': '8:40 - 10:15',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '42'
            },
            {
                'number': 2,
                'time': '10:35 - 12:10',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '43'
            },
            {
                'number': 3,
                'time': '12:20 - 13:55',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '44'
            },
            {
                'number': 4,
                'time': '14:05 - 15:40',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '45'
            },
            {
                'number': 5,
                'time': '15:50 - 17:25',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '46'
            },
            {
                'number': 6,
                'time': '17:35 - 20:10',
                'name': 'Вступ до університетських студій',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': None,
                'cabinet': '47'
            }
        ]
    else:
        is_online = True
        lessons = [{
                'number': 2,
                'time': '10:35 - 12:10',
                'name': 'Теорія ймовірностей',
                'teachers': ['доц. Пупків І.І.', 'проф. Іванов І.І.'],
                'link': 'https://zoom.us/blablabla',
                'cabinet': None
            }]
    return {
        'date': date,
        'faculty': faculty,
        'specialty': specialty,
        'course': course,
        'group': group,
        'is_online': is_online,
        'lessons': lessons
    }


if __name__ == '__main__':
    uvicorn.run(
        app,
        host="0.0.0.0",
        port=3000,
        log_level="debug",
    )
