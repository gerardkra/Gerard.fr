TT <- 1000
wn <- rnorm(TT)
plot(wn)
adf.test(wn)

wnt<-wn
for ( i in 4:TT)
{
  wnt[i]=wnt[i-1]/4+2*wnt[i-2]/4+wnt[i-3]/4+wn[i]
}
png('non-stationnaire-01.png')
plot(wnt)
dev.off()
adf.test(wnt)

