# Requisitos: Python 3.10+, discord.py 2.x, python-dotenv



import os

import json

import re

import random

import string

import asyncio

from datetime import datetime, timedelta, timezone



import discord

from discord import app_commands

from discord.ext import commands

from discord.utils import utcnow

from dotenv import load_dotenv