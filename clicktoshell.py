import sys
import os
import re


def clean_phone(data):
  """ Returns an international phone number for many common formats """

  simplified = data.strip()

  # Us phone numbers: (217) 352-1913
  if re.search(r"^\([0-9]{3}\)\s*[0-9]{3}\s*\-\s*[0-9]{4}$", simplified):
    simplified = "+1" + simplified

  # Us phone numbers: 217-352-1913
  if re.search(r"^[0-9]{3}\s*\-\s*[0-9]{3}\s*\-\s*[0-9]{4}$", simplified):
    simplified = "+1" + simplified

  # Manage phones like +32 (0) 80 41 81 54
  if simplified.startswith("+"):
    simplified = re.sub(r"\(\s*0\s*\)", "", simplified)

  simplified = re.sub(r"[\(\)\-\.\s]", "", simplified)

  # Special case for phones like 33 (0)4 89 06 58 00
  if simplified.startswith("330") and len(simplified) == 12:
    simplified = "+33" + simplified[3:]

  # 33 1 346 678 32
  if simplified.startswith("33") and len(simplified) == 11:
    simplified = "+33" + simplified[2:]

  # 44 7918708773
  if simplified.startswith("44") and len(simplified) == 12:
    simplified = "+" + simplified

  # (+33) 09 81 01 99 31
  if simplified.startswith("+330"):
    simplified = "+33" + simplified[4:]

  if re.search(r"^\+?[0-9]{6,15}$", simplified):
    if simplified.startswith("00"):
      simplified = "+" + simplified[2:]
    elif simplified.startswith("0"):
      simplified = "+33" + simplified[1:]  # Historical french default

  return simplified

  return None


protocol, raw_phone = sys.argv[1].split(":", 1)

template_file = os.path.expanduser("~/clicktoshell-%s.sh" % protocol)

phone = clean_phone(raw_phone)

if os.path.isfile(template_file):
  os.system("sh %s '%s'" % (template_file, phone))
