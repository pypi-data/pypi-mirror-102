import re
import math
import random
from functools import lru_cache
from typing import Tuple, Union

import _pyfxr
from _pyfxr import SoundBuffer, Wavetable, sfx

__all__ = (
    'SoundBuffer',
    'Wavetable',

    'sfx',
    'pickup',
    'laser',
    'explosion',
    'powerup',
    'hurt',
    'jump',
    'select',

    'tone',
    'pluck',
    'note_to_hertz',
)


NOTE_PATTERN = re.compile(r'^([A-G])([b#]?)([0-8])$')

A4 = 440.0

NOTE_VALUE = dict(C=-9, D=-7, E=-5, F=-4, G=-2, A=0, B=2)

TWELTH_ROOT = math.pow(2, (1 / 12))


@lru_cache()
def note_to_hertz(note: str) -> float:
    """Get a frequency for a given note.

    Here we use an even temper - all semitones in the octave are equally
    spaced twelfth powers of 2.

    """
    note, accidental, octave = validate_note(note)
    value = note_value(note, accidental, octave)
    return A4 * math.pow(TWELTH_ROOT, value)


def note_value(note: str, accidental: str, octave: int) -> int:
    """Given a note name, an accidental and an octave, return a note number.

    Each number corresponds to a specific note and can be converted to a pitch.
    """
    value = NOTE_VALUE[note]
    if accidental:
        value += 1 if accidental == '#' else -1
    return (4 - octave) * -12 + value


def validate_note(note: str) -> Tuple[str, str, int]:
    match = re.match(NOTE_PATTERN, note)
    if match is None:
        raise InvalidNote(
            '%s is not a valid note. '
            'notes are A-F, are either normal, flat (b) or sharp (#) '
            'and of octave 0-8' % note
        )
    note, accidental, octave = match.group(1, 2, 3)
    return note, accidental, int(octave)


def pluck(
    duration: float,
    pitch: Union[float, str],
    release: float = 0.1
) -> SoundBuffer:
    """Generate a pluck sound, like a harp or guitar."""
    # This is a wrapper to handle converting a note string to a pitch
    if isinstance(pitch, str):
        pitch = note_to_hertz(pitch)
    return _pyfxr.pluck(duration, pitch, release)


pluck.__doc__ = _pyfxr.pluck.__doc__


def tone(
    pitch: Union[float, str] = 440.0,  # Hz, default = A
    attack: float = 0.1,
    decay: float = 0.1,
    sustain: float = 0.75,
    release: float = 0.25,
    wavetable: Wavetable = Wavetable.sine(),
) -> SoundBuffer:
    """Generate a tone using a wavetable.

    The tone will be modulated by an ADSR envelope
    (attack-decay-sustain-release) which gives the tone a more natural feel,
    and avoids clicks when played. The total length of the tone is the sum of
    these durations.

    :param wavetable: The wavetable to use (default is a sine wave).
    :param pitch: The pitch of the tone to generate, either float Hz or a note
                  name/number like ``Bb4`` for B-flat in the 4th octave.
    :param attack: Attack time in seconds
    :param decay: Decay time in seconds
    :param sustain: Sustain time in seconds
    :param release: Release time in seconds

    """
    # This is a wrapper to handle converting a note string to a pitch
    if isinstance(pitch, str):
        pitch = note_to_hertz(pitch)
    return _pyfxr.tone(
        wavetable,
        pitch,
        attack * 44100,
        decay * 44100,
        sustain * 44100,
        release * 44100,
    )


def one_in(n: int) -> bool:
    """Return True with odds of 1 in n."""
    return not random.randint(0, n)


def pickup() -> SoundBuffer:
    """Generate a random pickup sound."""
    p_base_freq = random.uniform(0.4, 0.9)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.0, 0.1)
    p_env_decay = random.uniform(0.1, 0.5)
    p_env_punch = random.uniform(0.3, 0.6)
    if one_in(2):
        p_arp_mod = random.uniform(0.2, 0.6)
    return sfx(
        **locals()
    )


def laser() -> SoundBuffer:
    """Generate a random laser sound."""
    wave_type = random.choice((0, 0, 1, 1, 2))
    p_base_freq = random.uniform(0.5, 1.0)
    p_freq_limit = max(0.2, p_base_freq - random.uniform(0.2, 0.8))
    p_freq_ramp = random.uniform(-0.35, -0.15)
    if one_in(3):
        p_base_freq = random.uniform(0.3, 0.9)
        p_freq_limit = random.uniform(0.0, 0.1)
        p_freq_ramp = random.uniform(-0.65, -0.35)
    if one_in(2):
        p_duty = random.uniform(0.0, 0.5)
        p_duty_ramp = random.uniform(0.0, 0.2)
    else:
        p_duty = random.uniform(0.4, 0.9)
        p_duty_ramp = random.uniform(-0.7, 0.0)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.1, 0.3)
    p_env_decay = random.uniform(0.0, 0.4)
    if one_in(2):
        p_env_punch = random.uniform(0.0, 0.3)
    if one_in(3):
        p_pha_offset = random.uniform(0.0, 0.2)
        p_pha_ramp = random.uniform(-0.2, 0.0)
    if one_in(2):
        p_hpf_freq = random.uniform(0.0, 0.3)

    return sfx(
        **locals()
    )


def explosion() -> SoundBuffer:
    """Generate a random explosion sound."""
    wave_type = 3
    if one_in(2):
        p_base_freq = random.uniform(0.1, 0.5) ** 2
        p_freq_ramp = random.uniform(-0.1, 0.3)
    else:
        p_base_freq = random.uniform(0.2, 0.7) ** 2
        p_freq_ramp = random.uniform(-0.4, -0.2)
    if one_in(5):
        p_freq_ramp = 0
    if one_in(3):
        p_repeat_speed = random.uniform(0.3, 0.8)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.1, 0.4)
    p_env_decay = random.uniform(0.0, 0.5)
    if one_in(2):
        p_pha_offset = random.uniform(-0.3, 0.6)
        p_pha_ramp = random.uniform(-0.3, 0)
    p_env_punch = random.uniform(0.2, 0.6)
    if one_in(2):
        p_vib_strength = random.uniform(0.0, 0.7)
        p_vib_speed = random.uniform(0.0, 0.6)
    if one_in(3):
        p_arp_speed = random.uniform(0.6, 0.9)
        p_arp_mod = random.uniform(-0.8, 0.8)

    return sfx(
        **locals()
    )


def powerup() -> SoundBuffer:
    if one_in(2):
        wave_type = 1
    else:
        p_duty = random.uniform(0.0, 0.6)

    if one_in(2):
        p_base_freq = random.uniform(0.2, 0.5)
        p_freq_ramp = random.uniform(0.1, 0.5)
        p_repeat_speed = random.uniform(0.4, 0.8)
    else:
        p_base_freq = random.uniform(0.2, 0.5)
        p_freq_ramp = random.uniform(0.05, 0.25)
        if one_in(2):
            p_vib_strength = random.uniform(0.0, 0.7)
            p_vib_speed = random.uniform(0.0, 0.6)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.0, 0.4)
    p_env_decay = random.uniform(0.1, 0.5)

    return sfx(
        **locals()
    )


def hurt() -> SoundBuffer:
    wave_type = random.choice([0, 1, 3])
    if wave_type == 0:
        p_duty = random.uniform(0, 0.6)
    p_base_freq = random.uniform(0.2, 0.8)
    p_freq_ramp = random.uniform(-0.7, -0.3)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.0, 0.1)
    p_env_decay = random.uniform(0.1, 0.3)
    if one_in(2):
        p_hpf_freq = random.uniform(0.0, 0.3)

    return sfx(
        **locals()
    )


def jump() -> SoundBuffer:
    wave_type = 0
    p_duty = random.uniform(0.0, 0.6)
    p_base_freq = random.uniform(0.3, 0.6)
    p_freq_ramp = random.uniform(0.1, 0.3)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.1, 0.4)
    p_env_decay = random.uniform(0.1, 0.3)
    if one_in(2):
        p_hpf_freq = random.uniform(0.0, 0.3)
    if one_in(2):
        p_lpf_freq = random.uniform(0.4, 1.0)

    return sfx(
        **locals()
    )


def select() -> SoundBuffer:
    wave_type = random.choice([0, 1])
    if wave_type == 0:
        p_duty = random.uniform(0.0, 0.6)
    p_base_freq = random.uniform(0.2, 0.6)
    p_env_attack = 0.0
    p_env_sustain = random.uniform(0.1, 0.2)
    p_env_decay = random.uniform(0.0, 0.2)
    p_hpf_freq = 0.1
    return sfx(
        **locals()
    )
