def maker(N):
        def action(X):                
            return X ** N            
        return action


f  = maker(2)
print(f)
# What we get back is a reference to the nested function built—the one created and assigned to action when the nested def runs. If we now call what we got back from the outer function:

print(f(3))
print(f(4))