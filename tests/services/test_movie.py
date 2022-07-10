import pytest

from service.movie import MovieService


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movie_service(self, movie_dao):
        self.movie_service = MovieService(dao=movie_dao)

    def test_get_one(self):
        movie = self.movie_service.get_one(1)
        assert movie is not None
        assert isinstance(movie.id, int)
        assert movie.title == "Movie_1"

    def test_get_all(self):
        movies = self.movie_service.get_all()
        assert len(movies) > 0

    def test_create(self):
        movies_d = {"name": "New Name"}
        new_movie = self.movie_service.create(movies_d)
        assert new_movie.id is not None
        assert new_movie.title == "Movie_3"
        assert new_movie.genre_id == 1
        assert new_movie.trailer == "..."

    def test_update(self):
        movie = self.movie_service.update(1)

    def test_delete(self):
        result = self.movie_service.delete(1)
        assert result is None
