start = h:integer ':'? m:integer? isP:ampm? {
  let hour = isP ? 12+h : h
  return 60*hour + m
}
integer = d:[0-9]+ {return parseInt(d.join(''))}
ampm = ap:('a'/'p') 'm' {return 'p'===ap}
