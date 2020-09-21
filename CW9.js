function zeros (n) {
  let i = 1
  let res = 0
  while (n >= i) {
    i *= 5
    res += Math.floor(n/i)
  }
  return res
}

zeros(30)