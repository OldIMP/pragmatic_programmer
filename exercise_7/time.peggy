start = h:digits m:(':' @digits)? ap:ampm?
        &{return m||ap}
        {
          let hour = 'pm'===ap ? 12+h : h
          return 60*hour + m
        }
digits = d:$[0-9]|1..2| {return parseInt(d)}
ampm = $'am'/'pm'
