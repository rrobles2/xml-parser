from lxml import etree

class Class:  
  def __init__(self, inName):
    self.name=inName
    self.description=None
    self.internalid=None
    self.source=None
    self.revisiondate=None
    self.flavor=None
    self.keyAbilities=None
    self.implements=None
    self.armorProf=None
    self.weaponProf=None
    self.defbonus=None
    self.hp1st=None
    self.hpperlvl=None
    self.surges=None
    self.trainedSkills=None
    self.classSkills=None
    self.buildOptions=None
    self.parsedClassFeature=None
    self.role=None
    self.powersource=None
    self.creating=None
    self.classFeatures=None
    self.supplemental=None
    self.implement=None
    self.powers=None
    self.powerName=None
    self.roleElement=None
    self.powerSourceElement=None
    self.secondaryPowerSourceElement=None
    self.secondaryAbilities=None
    self.hybridTalentOptions=None
    self.shortDescription=None
    self.parentClass=None
    self.traitPackage=None
    self.rules=None
    
  def parseFields(self, xml):
    self.internalid=xml.get('internal-id')
    if not self.internalid == None:
      print "internal-id: "+self.internalid
    
    self.source=xml.get('source')
    if not self.source == None:
      print "source: "+self.source
    
    self.revisiondate=xml.get('revision-date')
    if not self.revisiondate == None:
      print "revision-date: "+self.revisiondate

    holdChildren = xml.getchildren()
    for holdChild in holdChildren:
      if holdChild.tag == "rules":
        self.description = holdChild.tail.encode("utf-8")
        print "Desc: "+self.description