program Force

implicit none

integer,parameter :: n=100
integer:: i,j
real :: R(n,3), dr(3), rho, f(3*n,n), dU(n,n), TF(3*n), FM(n)



! Parameters
! n = 100 # particle number
 
  
 
 call init_random_seed()
 call RANDOM_NUMBER(R) ! random init pos matrix


dU(:,:)=0
dr(:)=0
f(:,:)=0
TF(:)=0
FM(:)=0

do i=1,n
    do j=1,n
            
	if (i < j) then
                
         dr(:) = R(i,:) - R(j,:)   !dx,dy,dz are elements of difference vector r_ij       
         
                
         rho = dot_product(dr,dr)**0.5   ! length of r_ij
                
         dU(i,j) = (12*rho**(-13) - 6*rho**(-7)) * rho**(-1) ! grad U
                
         f(i,j) = dU(i,j) * dr(1)
         f((n+i),j) = dU(i,j) * dr(2)
         f((2*n+i),j) = dU(i,j) * dr(3) 
         !fy(i,j) = dU(i,j) * dy(i,j)
         !fz(i,j) = dU(i,j) * dz(i,j)
         
         
         f(j,i) = -f(i,j)
         f(j,(n+i)) = -f((n+i),j)
         f(j,(2*n+i)) = -f((2*n+i),j) 
         
         
	 !fx(j,i)=-fx(i,j)
	 !fy(j,i)=-fy(i,j)
	 !fz(j,i)=-fz(i,j)

	 !dx(j,i)=dx(i,j)
	 !dy(j,i)=dy(i,j)
	 !dz(j,i)=dz(i,j)


	 end if
	

      end do
 end do


TF(:)=sum(f,2)
do i=1,n

    FM(i)=(TF(i)**2 + TF(n+i)**2 + TF(2*n+i)**2)**0.5

end do
print *, FM

end program
    
SUBROUTINE init_random_seed()
            INTEGER :: l, k, clock
            INTEGER, DIMENSION(:), ALLOCATABLE :: seed
          
            CALL RANDOM_SEED(size = k)
            ALLOCATE(seed(k))
          
            CALL SYSTEM_CLOCK(COUNT=clock)
          
            seed = clock + 37 * (/ (l - 1, l = 1, k) /)
            CALL RANDOM_SEED(PUT = seed)
          
            DEALLOCATE(seed)
END SUBROUTINE init_random_seed    

