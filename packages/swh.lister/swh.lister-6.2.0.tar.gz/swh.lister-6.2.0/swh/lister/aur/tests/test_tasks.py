# Copyright (C) 2022  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from swh.lister.pattern import ListerStats


def test_aur_ping(swh_scheduler_celery_app, swh_scheduler_celery_worker):
    res = swh_scheduler_celery_app.send_task("swh.lister.aur.tasks.ping")
    assert res
    res.wait()
    assert res.successful()
    assert res.result == "OK"


def test_aur_lister(swh_scheduler_celery_app, swh_scheduler_celery_worker, mocker):
    # setup the mocked AurLister
    lister = mocker.patch("swh.lister.aur.tasks.AurLister")
    lister.from_configfile.return_value = lister
    stats = ListerStats(pages=42, origins=42)
    lister.run.return_value = stats

    res = swh_scheduler_celery_app.send_task("swh.lister.aur.tasks.AurListerTask")
    assert res
    res.wait()
    assert res.successful()
    assert res.result == stats.dict()

    lister.from_configfile.assert_called_once_with()
    lister.run.assert_called_once_with()
