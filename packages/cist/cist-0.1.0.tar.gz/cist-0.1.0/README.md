# python-cist

![GitHub-issues](https://img.shields.io/github/issues/WWFyb3NsYXYg/python-cist)
<p align="right">
<img src="https://github.com/WWFyb3NsYXYg/python-cist/assets/87089735/aa557eb3-24d0-44fe-b4ea-307004316d12">
<p>
Python client for CIST API (https://cist.nure.ua)

## Installation

```
pip install cist
```


# Usage

## For group (Couples schedule is for group only. More see `Couples` for details)

1) Get your group id:
```python
  import cist

  groups = cist.get_groups()
  print(groups)
```
2) Use that group_id to initialize client:

```python
  import cist
  group_id = 'xxxxxxxx'

  group = cist.Group(group_id)
  group_schedule = group.get_schedule()
  print(group_schedule)
```
## For teachers (Couples schedule is for teacher only. More see `Couples` for details)

1) Get your teachers id:
```python
  import cist

  struct = cist.get_struct()
  print(struct)
```
2) Use that teacher_id to initialize client:

```python
  import cist
  teacher_id = 'xxxxxxxx'

  teacher = cist.Teacher(teacher_id)
  teacher_schedule = teacher.get_schedule()
  print(teacher_schedule)
```
## For audience (Couples schedule is for audience only. More see `Couples` for details)

1) Get audience id:
```python
  import cist

  audiences = cist.get_audiences()
  print(audiences)
```
2) Use that audience_id to initialize client:

```python
  import cist
  audience_id = 'xxxxxxxx'

  audience = cist.Auditory(group_id)
  audience_schedule = grouaudiencep.get_schedule()
  print(audience_schedule)
```

## Couples
Schedule of events (couples), for the teacher, groups or audiences. `A couple is a fact of meeting in time and space/audience of interested individuals/groups/teachers with a certain purpose/subject.` On one couple, an academic group can be several disciplines at the same time (overlays), this is acceptable for alternative disciplines. Unique is the combination “couple time + discipline".

- `timetable_id` – group or teacher id
- `type_id`: 1 – group (default), 2 – teacher, 3 – audience
- `time_from` – start date of sampling from schedule (default – start current semester)
- `time_to` – end date of sampling from schedule (default – end current semester).

```python
  import cist
  timetable_id = 'xxxxxxxx'
  type_id = 2
  time_from = date(2023,11,17)
  time_to = date(2023,11,18)

  timetable = cist.Couple(timetable_id, type_id)
  event_schedule = timetable.get_schedule(time_from, time_to)
  print(event_schedule)
```
## Information about a specific object

Groups of the same direction (optional within the faculty)

```python
  id_direction = 'xxxxxxxx'
  id_faculty = 'xxxxxxxx'	#not necessary

  object = cist.Object(id_direction, id_faculty)

  grp_of_directions = object.get_grp_of_directions()
  print(grp_of_directions)
```

Specialty groups (optional within the faculty department)

```python
  id_speciality = 'xxxxxxxx'
  id_faculty = 'xxxxxxxx' 	#not necessary

  object = cist.Object(id_speciality, id_faculty)

  grp_of_specialities = object.get_grp_of_specialities()
  print(grp_of_specialities)
```

All specialties of a specific direction related to a specific faculty (relevant for specialists and masters)

```python
  id_direction = 'xxxxxxxx'
  id_faculty = 'xxxxxxxx' 

  object = cist.Object(id_direction, id_faculty)

  specialities = object.get_specialities()
  print(specialities)
```

All areas of the faculty

```python
  id_faculty = 'xxxxxxxx' 

  object = cist.Object(id_faculty)

  directions = object.get_directions()
  print(directions)
```

All teachers of the department

```python
  id_department = 'xxxxxxxx' 

  object = cist.Object(id_department)

  teachers = object.get_teachers()
  print(teachers)
```

All departments of the faculty

```python
  id_faculty = 'xxxxxxxx' 

  object = cist.Object(id_faculty)

  departments = object.get_departments()
  print(departments)
```


### Methods

Get the entire structure of the university with faculties,
directions, specialties and groups
students. Destinations include only
groups of bachelors. For groups of specialists and
Master's degrees are related to
specialties that are included in the directions

```python
>>> cist.get_groups()

```

Get the entire structure of the university with faculties,
departments, teachers.

```python
>>> cist.get_struct()

```
Get the entire structure of the university with buildings,
audiences and types of audiences. Audiences
located in buildings. Every audience
may refer to zero, one or
several types.

```python
>>> cist.get_audiences()

```
Get all university faculties

```python
>>> cist.get_faculties()

```

Get all types of university classrooms

```python
>>> cist.get_audiences_types()

```
Get help

```python
>>> cist.help()

```




You can as well pass datetime objects ``get_schedule(time_from, time_to)``
```python
>>> group.get_schedule(date(2023,11,17), date(2023,11,17))
```


You can use ratelimiter library (like https://pypi.org/project/ratelimiter/ )
