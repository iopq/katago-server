import os
from enum import Enum

import uuid as uuid
from django.contrib.postgres.fields import JSONField
from django.db.models import Model, CharField, DecimalField, IntegerField, FileField, BooleanField, DateTimeField, \
    ForeignKey, PROTECT, BigAutoField, UUIDField, TextChoices, TextField
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel

from katago_server.contrib.validators import FileValidator
from katago_server.games.models import RankingEstimationGame, TrainingGame
from katago_server.trainings.models import Network
from katago_server.users.models import User


def upload_initial_to(instance, filename):
    return os.path.join("initial_position", f"{instance.uuid}.sgf")


validate_sgf = FileValidator(max_size=1024*1024*10, magic_types=("Smart Game Format (Go)",))


class DistributedTask(Model):
    """
    This class holds a predefined job that will be given in priority to fast client
    """
    class Meta:
        abstract = True

    class Status(TextChoices):
        UNASSIGNED = "UNASSIGNED", _("Unassigned")
        ONGOING = "ONGOING", _("Ongoing")
        DONE = "DONE", _("Done")
        CANCELED = "CANCELED", _("Canceled")

    # We expect a large number of "DistributedTasks" so lets use BigInt
    id = BigAutoField(primary_key=True)
    uuid = UUIDField(_("unique identifier"), default=uuid.uuid4)
    status = CharField(_("task status"), max_length=15, choices=Status.choices, null=False, default=Status.UNASSIGNED)
    # a predefined task  get attributed to an user with some expiration
    created_at = DateTimeField(_("creation date"), auto_now_add=True)
    assigned_to = ForeignKey(User,  verbose_name=_("assigned to"), on_delete=PROTECT, related_name='%(class)s_games', blank=True, null=True)
    assigned_at = DateTimeField(_("assignation date"), auto_now=True, blank=True, null=True)
    expire_at = DateTimeField(_("expiration date"), blank=True, null=True)
    # The networks related to this game
    white_network = ForeignKey(Network, verbose_name=_("network white"), on_delete=PROTECT, related_name='%(class)s_predefined_jobs_as_white')
    black_network = ForeignKey(Network, verbose_name=_("network black"),  on_delete=PROTECT, related_name='%(class)s_predefined_jobs_as_black')
    # Describe the board/game itself
    board_size_x = IntegerField(_("board absciss"), default=19)
    board_size_y = IntegerField(_("board ordinate"), default=19)
    handicap = IntegerField(_("nb of handicap stone"), default=0)
    komi = DecimalField(_("komi (white)"), max_digits=3, decimal_places=1, default=7.0)
    # -- Everything under is nullable --
    rules_params = JSONField(_("game rules"), help_text=_("Depending on rule set, the ko (https://senseis.xmp.net/?Ko), the scoring (https://senseis.xmp.net/?Scoring), the group tax (https://senseis.xmp.net/?GroupTax) and the suicide (https://senseis.xmp.net/?Suicide) may have subtle difference. See more info here https://lightvector.github.io/KataGo/rules.html"), default=dict, null=True, blank=True)  # See https://lightvector.github.io/KataGo/rules.html
    # A PredefinedJob can be forked from an existing game or a initial situation
    initial_position_sgf_file = FileField(_("initial position, as sgf file"), upload_to=upload_initial_to, validators=(validate_sgf,), null=True, blank=True)
    initial_position_extra_params = JSONField(_("initial position extra parameters"), default=dict, null=True, blank=True)
    # Some extra information about the game like the type
    # eg: komi compensated games, uncompensated games, asymmetric playout games, seki-training games
    game_extra_params = JSONField(_("extra game parameters regarding game, like number of playout"), default=dict, null=True, blank=True)

    def __str__(self):
        return f"{self.uuid}"


class RankingEstimationGameDistributedTask(DistributedTask):
    # The result of a "DONE" RankingGameDistributedTask is a Game
    resulting_game = ForeignKey(RankingEstimationGame, verbose_name=_("resulting ranking game"), on_delete=PROTECT, null=True, blank=True)


class TrainingGameDistributedTask(DistributedTask):
    # The result of a "DONE" RankingGameDistributedTask is a Game
    resulting_game = ForeignKey(TrainingGame, verbose_name=_("resulting training game"), on_delete=PROTECT, null=True, blank=True)


class DynamicDistributedTaskConfiguration(SingletonModel):
    def __str__(self):
        return "Katago Configuration"

    class Meta:
        verbose_name = "Katago Configuration"

    katago_config = TextField()