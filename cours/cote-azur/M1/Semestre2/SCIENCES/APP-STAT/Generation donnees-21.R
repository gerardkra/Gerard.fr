simulnormb=function(nbdata,mx=c(-7,0,7),my=c(-5,5),sd=2)
	{
	i1=sample(1:length(mx),nbdata,replace=TRUE)
	j1=sample(1:length(my),nbdata,replace=TRUE)
	Data=cbind(rnorm(nbdata,mx[i1],sd),rnorm(nbdata,my[j1],sd))
#    Noise=cbind(rnorm(round(nbdata/10),0,8),rnorm(round(nbdata/10),0,8))
#    Data=rbind(Data,Noise)
	realclust=10*i1+j1
#    realclust=c(realclust,rep(max(realclust)+1,nrow(Noise)))
        
#    return(cbind(realclust,Data))
	return(cbind(Data,realclust))
}