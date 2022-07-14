from datetime import datetime
import requests
from bs4 import BeautifulSoup
from sqlalchemy.orm import Session
from transfer_to_bd import *
from hh_parser import get_jobs

get_jobs(".net+framework")

