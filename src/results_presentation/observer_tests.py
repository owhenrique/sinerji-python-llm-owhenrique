import pytest
from unittest.mock import MagicMock
from observer import Observer, ResponseObserver, Subject

class TestSubject:
    def test_attach_observer(self):
        subject = Subject()
        observer = MagicMock(spec=Observer)
        subject.attach(observer)

        assert observer in subject._observers

    def test_detach_observer(self):
        subject = Subject()
        observer = MagicMock(spec=Observer)
        subject.attach(observer)
        subject.detach(observer)

        assert observer not in subject._observers

    def test_notify_observers(self):
        subject = Subject()
        observer1 = MagicMock(spec=Observer)
        observer2 = MagicMock(spec=Observer)
        subject.attach(observer1)
        subject.attach(observer2)

        subject.notify("Test message")

        observer1.update.assert_called_once_with("Test message")
        observer2.update.assert_called_once_with("Test message")


class TestResponseObserver:
    def test_update(self, capsys):
        observer = ResponseObserver()
        observer.update("Test message")

        captured = capsys.readouterr()
        assert captured.out == "Observer Notification: Test message\n"
