import pytest
from model_bakery import baker
from rest_framework.test import APIClient

from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course_create_fab(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_course_list(client, course_factory):
    course = course_factory(_quantity=10)

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    for i, c in enumerate(data):
        assert c['name'] == course[i].name


@pytest.mark.django_db
def test_course_filter_id(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?id={course[0].id}')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course[0].name


@pytest.mark.django_db
def test_course_filter_name(client, course_factory):
    course = course_factory(_quantity=10)
    response = client.get(f'/api/v1/courses/?name={course[0].name}')

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course[0].id


@pytest.mark.django_db
def test_course_create(client):
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', data={'name': 'Курс 1'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_course_update_fab(client, course_factory):
    course = course_factory(_quantity=1)

    response = client.patch(f'/api/v1/courses/{course[0].id}/', {
        'name': 'Курс 1'
    })

    assert response.status_code == 200
    data = response.json()
    assert data['name'] != course[0].name and data['name'] == 'Курс 1'


@pytest.mark.django_db
def test_course_delete(client, course_factory):
    course = course_factory(_quantity=1)
    count = Course.objects.count()
    response = client.delete(f'/api/v1/courses/{course[0].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == count - 1

