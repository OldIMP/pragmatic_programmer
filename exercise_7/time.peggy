start = h:digits m:min? ap:ampm?
        &{
          let isTime = m||ap
          let isHourValid = ap? 13>h : 25>h
          return isTime && isHourValid
        }
        {
          let hour = 'pm'===ap ? 12+h : h
          return 60*hour + m
        }
digits = d:$[0-9]|1..2| {return parseInt(d)}
min = ':' @m:digits &{return 60>m}
ampm = $'am'/'pm'
