start = h:digits ':'? m:digits? isP:ampm? {
  let hour = isP ? 12+h : h
  return 60*hour + m
}
digits = d:$[0-9]|1..2| {return parseInt(d)}
ampm = ap:('a'/'p') 'm' {return 'p'===ap}
