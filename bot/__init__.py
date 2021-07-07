"""
Author: Blane Lysak
Description: This is the 
"""

from active_alchemy import ActiveAlchemy

db = ActiveAlchemy("sqlite:///news_database.db")

db.create_all()