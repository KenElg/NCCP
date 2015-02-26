subroutine Force(n, L, rho_c, TF)

implicit none

INTEGER :: p, k, clock
INTEGER, DIMENSION(:), ALLOCATABLE :: seed
integer,intent(in) :: n, L 
real, intent(in) :: rho_c
real, intent(out) ::  TF(3*n)
integer:: i,j
real :: R(n,3), dr(3), rho, f(3*n,n), dU(n,n), FM(n)


! Parameters
! n = 100 # particle number
 
  
 
 CALL RANDOM_SEED(size = k)
 ALLOCATE(seed(k))
          
 CALL SYSTEM_CLOCK(COUNT=clock)
          
 seed = clock + 37 * (/ (p - 1, p = 1, k) /)
 CALL RANDOM_SEED(PUT = seed)
          
 DEALLOCATE(seed)

 call RANDOM_NUMBER(R) ! random init pos matrix


dU=0
dr=0
f=0
TF=0
FM=0

do i=1,n
    do j=1,n
            
	if (i < j) then
                
         dr(:) = R(i,:) - R(j,:)   !dx,dy,dz are elements of difference vector r_ij       
                
         rho = dot_product(dr,dr)**0.5   ! length of r_ij
         
         rho = rho - L * nint(rho/L)
         
         if (rho > rho_c) then       
         
         cycle
              
         end if 
         
         dU(i,j) = (12*rho**(-13) - 6*rho**(-7)) * rho**(-1) ! grad U
               
         f(i,j) = dU(i,j) * dr(1)
         f((n+i),j) = dU(i,j) * dr(2)
         f((2*n+i),j) = dU(i,j) * dr(3) 
         !fy(i,j) = dU(i,j) * dy(i,j)
         !fz(i,j) = dU(i,j) * dz(i,j)
         
         
         f(j,i) = -f(i,j)
         f(j,(n+i)) = -f((n+i),j)
         f(j,(2*n+i)) = -f((2*n+i),j) 
         


	 end if
	

      end do
 end do


TF(:)=sum(f,2)
do i=1,n

    FM(i)=(TF(i)**2 + TF(n+i)**2 + TF(2*n+i)**2)**0.5

end do
print *, TF

end subroutine
    
            
          
            
