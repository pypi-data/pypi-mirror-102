class Data_Prepare:
  def __init__(self, target, target_u, daypara):
    self.target = target
    self.target_u = target_u
    self.daypara = daypara

  def parse(func):         
    def wrap(self, target): 
      data = func(self, target)
      dit = {"Date":data.index, "price":data["Close"], "high":data["High"],"low":data["Low"],'vol':data["Volume"]}
      df = pd.DataFrame(dit)
      return df               
    return wrap 
  
  @parse
  def fetch(self, target):
    now = datetime.date.today()
    start = now - datetime.timedelta(days = int(self.daypara))
    data = data_reader.DataReader(target, "yahoo", str(start), str(now))
    return data

  def diff_data(self, window):
    diff = self.fetch(target_u)["price"].diff()[window:]
    return diff