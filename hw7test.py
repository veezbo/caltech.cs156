from sklearn import svm

X = [[0, 0], [1, 1], [0.5, 0.5], [0.12, .9123]]
y = [-1, 1, -1, 1]
clf = svm.SVC( kernel='linear', C=1.0E6 )
clf.fit(X, y)

print clf
print clf.n_support_
print clf.coef_

score = clf.score( [ 0.2213, -0.2301 ], [ 1 ] )
e_out = abs(score - 1.0)

print score
print e_out