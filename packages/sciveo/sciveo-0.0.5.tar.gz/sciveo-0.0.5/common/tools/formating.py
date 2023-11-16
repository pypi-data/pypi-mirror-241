#
# Pavlin Georgiev, Softel Labs
#
# This is a proprietary file and may not be copied,
# distributed, or modified without express permission
# from the owner. For licensing inquiries, please
# contact pavlin@softel.bg.
#
# 2023
#

def format_elapsed_time(seconds):
  time_units = [('d', 86400), ('h', 3600), ('m', 60), ('s', 1)]
  components = []
  for unit, factor in time_units:
    count = seconds // factor
    if count > 0:
      components.append(f"{int(count)}{unit}")
    seconds %= factor
  formatted_time = ' '.join(components)
  return formatted_time
