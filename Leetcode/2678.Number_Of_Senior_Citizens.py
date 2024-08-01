def countSeniors(details: list[str]) -> int:
  count = 0
  for detail in details:
    if int(detail[11:13]) > 60: 
      count += 1
   
  return count
  
details = ["7868190130M7522","5303914400F9211","9273338290F4010"]
print(countSeniors(details))