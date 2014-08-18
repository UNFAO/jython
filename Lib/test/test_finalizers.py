'''
Created on 06.08.2014
'''

import platform
import unittest
import types
import time
if platform.system() == "Java":
	from java.lang import System
	from org.python.core.finalization import FinalizeTrigger

class GCDetector():
	gcIndex = 0
	
	def __del__(self):
		GCDetector.gcIndex += 1

maxGCRun = 10

def runGCIfJython():
	if platform.system() == "Java":
		currentIndex = GCDetector.gcIndex
		gcCount = 0
		detector = GCDetector()
		detector = None
		while currentIndex == GCDetector.gcIndex and gcCount < maxGCRun:
			System.gc()
			gcCount += 1
			time.sleep(0.1)

finalizeMsgList = []
verbose = False
resurrectedObject_I = None
resurrectedObject_J = None
resurrectedObject_K = None
resurrectedObject_L = None
resurrectedObject_M = None
resurrectedObject_N = None

class ResurrectableDummyClass():

	def __init__(self, name):
		self.name = name
		self.doResurrection = True

	def __str__(self):
		return self.name


class ResurrectableDummyClassNew(object):

	def __init__(self, name):
		self.name = name
		self.doResurrection = True

	def __str__(self):
		return self.name


def __del__I(self):
	global resurrectedObject_I
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_I = self

def __del__J(self):
	global resurrectedObject_J
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_J = self

def __del__K(self):
	global resurrectedObject_K
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_K = self

def __del__L(self):
	global resurrectedObject_L
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_L = self

def __del__M(self):
	global resurrectedObject_M
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_M = self

def __del__N(self):
	global resurrectedObject_N
	finalizeMsgList.append(str(self)+" finalized (ResurrectableDummyClass)")
	if verbose:
		print str(self)+" finalized (ResurrectableDummyClass)"
	if self.doResurrection:
		resurrectedObject_N = self

delI = __del__I
delJ = __del__J
delK = __del__K
delL = __del__L
delM = __del__M
delN = __del__N


class DummyClass():
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name


class DummyClassDel():
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name
	
	def __del__(self):
		finalizeMsgList.append(str(self)+" finalized (DummyClassDel)")
		if verbose:
			print str(self)+" finalized (DummyClassDel)"


class DummyClassNew(object):
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name

class DummyClassDelNew(object):
	
	def __init__(self, name):
		self.name = name
	
	def __str__(self):
		return self.name
	
	def __del__(self):
		finalizeMsgList.append(str(self)+" finalized (DummyClassDelNew)")
		if verbose:
			print str(self)+" finalized (DummyClassDelNew)"

class DummyFileClassNew(file):
	
	def __init__(self, name):
		self.name0 = name
	
	def __str__(self):
		return self.name0

	def __del__(self):
		finalizeMsgList.append(str(self)+" finalized (DummyFileClassNew)")
		if verbose:
			print str(self)+" finalized (DummyFileClassNew)"


def __del__class(self):
	finalizeMsgList.append(str(self)+" finalized (acquired by class)")
	if verbose:
		print str(self)+" finalized (acquired by class)"

def __del__object(self):
	finalizeMsgList.append(str(self)+" finalized (acquired by object)")
	if verbose:
		print str(self)+" finalized (acquired by object)"

def __del__object0():
	finalizeMsgList.append("_ finalized (acquired by object)")
	if verbose:
		print "_ finalized (acquired by object)"

delClass = __del__class
delObject = __del__object
delObject0 = __del__object0

class TestFinalizers(unittest.TestCase):
	def test_finalizer_builtin_oldStyleClass(self):
		A = DummyClassDel("A")
		A = None
		runGCIfJython()
		assert("A finalized (DummyClassDel)" in finalizeMsgList)

	def test_classAcquiresFinalizer_beforeInstanciation_oldStyleClass(self):
		DummyClass.__del__ = delClass
		B = DummyClass("B")
		B = None
		runGCIfJython()
		assert("B finalized (acquired by class)" in finalizeMsgList)
		del DummyClass.__del__

	def test_classAcquiresFinalizer_afterInstanciation_oldStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer call
		C = DummyClass("C")
		DummyClass.__del__ = delClass
		if platform.system() == "Java":
			FinalizeTrigger.ensureFinalizer(C)
		C = None
		runGCIfJython()
		assert("C finalized (acquired by class)" in finalizeMsgList)
		del DummyClass.__del__

	def test_instanceAcquiresFinalizer_bound_oldStyleClass(self):
		D = DummyClassDel("D")
		dl = types.MethodType(delObject, D.name)
		D.__del__ = dl
		D = None
		runGCIfJython()
		assert("D finalized (DummyClassDel)" not in finalizeMsgList)
		assert("D finalized (acquired by object)" in finalizeMsgList)

	def test_finalizer_builtin_newStyleClass(self):
		E = DummyClassDelNew("E")
		E = None
		runGCIfJython()
		assert("E finalized (DummyClassDelNew)" in finalizeMsgList)

	def test_classAcquiresFinalizer_beforeInstanciation_newStyleClass(self):
		DummyClassNew.__del__ = delClass
		F = DummyClassNew("F")
		F = None
		runGCIfJython()
		assert("F finalized (acquired by class)" in finalizeMsgList)
		del DummyClassNew.__del__

	def test_classAcquiresFinalizer_afterInstanciation_newStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer call
		G = DummyClassNew("G")
		DummyClassNew.__del__ = delClass
		if platform.system() == "Java":
			FinalizeTrigger.ensureFinalizer(G)
		G = None
		runGCIfJython()
		assert("G finalized (acquired by class)" in finalizeMsgList)
		del DummyClassNew.__del__

	def test_instanceAcquiresFinalizer_bound_newStyleClass(self):
		"""
		It seems, CPython prohibits new style instances from acquiring a finalizer.
		"""
		H = DummyClassDelNew("H")
		H.__del__ = types.MethodType(delObject, H.name)
		H = None
		runGCIfJython()
		assert("H finalized (DummyClassDelNew)" in finalizeMsgList)
		assert("H finalized (acquired by object)" not in finalizeMsgList)

	def test_instanceAcquiresFinalizer_bound_newStyleClass2(self):
		"""
		It seems, CPython prohibits new style instances from acquiring a finalizer.
		If one calls the instance-acquired __del__ manually, it works, but the gc
		will still call the old one.
		"""
		H = DummyClassDelNew("H2")
		H.__del__ = types.MethodType(delObject, H.name)
		H.__del__()
		H = None
		runGCIfJython()
		assert("H2 finalized (DummyClassDelNew)" in finalizeMsgList)
		assert("H2 finalized (acquired by object)" in finalizeMsgList)

	def test_objectResurrection_oldStyleClass(self):
		ResurrectableDummyClass.__del__ = delI
		I = ResurrectableDummyClass("I")
		I = None
		runGCIfJython()
		assert("I finalized (ResurrectableDummyClass)" in finalizeMsgList)
		assert(str(resurrectedObject_I) == "I")

	def test_objectDoubleResurrection_oldStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer calls
		ResurrectableDummyClass.__del__ = delJ
		J = ResurrectableDummyClass("J")
		J = None
		
		runGCIfJython()
		assert("J finalized (ResurrectableDummyClass)" in finalizeMsgList)
		global resurrectedObject_J
		assert(str(resurrectedObject_J) == "J")
		J = resurrectedObject_J
		resurrectedObject_J = None
		assert(resurrectedObject_J is None)
		if platform.system() == "Java":
			#For Jython one can restore the finalizer manually.
			#This is offered as an easy fix if the CPython behavior
			#in this test should be needed for some reason.
			FinalizeTrigger.ensureFinalizer(J)
		J = None

		runGCIfJython()
		assert(str(resurrectedObject_J) == "J")
		resurrectedObject_J.doResurrection = False
		if platform.system() == "Java":
			#again...
			FinalizeTrigger.ensureFinalizer(resurrectedObject_J)
		resurrectedObject_J = None
		
		runGCIfJython()
		assert(resurrectedObject_J is None)
		

	def test_objectDoubleResurrectionAndFinalize_oldStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer calls
		ResurrectableDummyClass.__del__ = delK
		K = ResurrectableDummyClass("K")
		K = None
		
		runGCIfJython()
		assert("K finalized (ResurrectableDummyClass)" in finalizeMsgList)
		finalizeMsgList.remove("K finalized (ResurrectableDummyClass)")
		assert("K finalized (ResurrectableDummyClass)" not in finalizeMsgList)
		global resurrectedObject_K
		assert(str(resurrectedObject_K) == "K")
		K = resurrectedObject_K
		resurrectedObject_K = None
		assert(resurrectedObject_K is None)
		if platform.system() == "Java":
			FinalizeTrigger.ensureFinalizer(K)
		K = None
		
		runGCIfJython()
		assert("K finalized (ResurrectableDummyClass)" in finalizeMsgList)
		assert(str(resurrectedObject_K) == "K")

	def test_objectResurrection_newStyleClass(self):
		ResurrectableDummyClassNew.__del__ = delL
		L = ResurrectableDummyClassNew("L")
		L = None
		runGCIfJython()
		assert("L finalized (ResurrectableDummyClass)" in finalizeMsgList)
		assert(str(resurrectedObject_L) == "L")

	def test_objectDoubleResurrection_newStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer calls
		ResurrectableDummyClassNew.__del__ = delM
		M = ResurrectableDummyClassNew("M")
		M = None

		runGCIfJython()
		assert("M finalized (ResurrectableDummyClass)" in finalizeMsgList)
		global resurrectedObject_M
		assert(str(resurrectedObject_M) == "M")
		M = resurrectedObject_M
		resurrectedObject_M = None
		assert(resurrectedObject_M is None)
		if platform.system() == "Java":
			FinalizeTrigger.ensureFinalizer(M)
		M = None

		runGCIfJython()
		assert(str(resurrectedObject_M) == "M")

	def test_objectDoubleResurrectionAndFinalize_newStyleClass(self):
		#okay to fail in Jython without the manual ensureFinalizer calls
		ResurrectableDummyClassNew.__del__ = delN
		N = ResurrectableDummyClassNew("N")
		N = None

		runGCIfJython()
		assert("N finalized (ResurrectableDummyClass)" in finalizeMsgList)
		finalizeMsgList.remove("N finalized (ResurrectableDummyClass)")
		assert("N finalized (ResurrectableDummyClass)" not in finalizeMsgList)
		global resurrectedObject_N
		assert(str(resurrectedObject_N) == "N")
		N = resurrectedObject_N
		resurrectedObject_N = None
		assert(resurrectedObject_N is None)
		if platform.system() == "Java":
			FinalizeTrigger.ensureFinalizer(N)
		N = None

		runGCIfJython()
		assert("N finalized (ResurrectableDummyClass)" in finalizeMsgList)
		assert(str(resurrectedObject_N) == "N")

	def test_file_overwrite_del(self):
		O = DummyFileClassNew("O")
		O = None

		runGCIfJython()
		assert("O finalized (DummyFileClassNew)" in finalizeMsgList)


if __name__ == '__main__':
	unittest.main()

