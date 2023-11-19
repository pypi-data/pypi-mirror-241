# libraries
import os
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit.Chem import Descriptors
from rdkit.Chem import Draw


# common functions

def cleanup_file():
    file_path = 'temp/molecule.pdb'
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted file: {file_path}")

def smiles_to_xyz(smiles_string):
    mol = Chem.MolFromSmiles(smiles_string)
    if mol is None:
        return None, 0, 0  # Return None to indicate that the conversion failed

    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.MMFFOptimizeMolecule(mol)

    charge = Chem.GetFormalCharge(mol)
    num_radicals = Descriptors.NumRadicalElectrons(mol)
    multiplicity = num_radicals + 1 

    xyz_str = ""
    for atom in mol.GetAtoms():
        pos = mol.GetConformer().GetAtomPosition(atom.GetIdx())
        xyz_str += "{}\t{}\t{}\t{}\n".format(atom.GetSymbol(), pos.x, pos.y, pos.z)

    return xyz_str, charge, multiplicity

def smiles_to_pdb(smiles_string):
    mol = Chem.MolFromSmiles(smiles_string)
    if mol is None:
        return None

    mol = Chem.AddHs(mol)
    AllChem.EmbedMolecule(mol, AllChem.ETKDG())
    AllChem.MMFFOptimizeMolecule(mol)

    pdb_str = Chem.MolToPDBBlock(mol)
    return pdb_str

def pdb_to_xyz_data(pdb_file):
        # Read the PDB file
        mol = Chem.MolFromPDBFile(pdb_file, removeHs=False, sanitize=False)
        if mol is None:
            return None, None, None
        # Add hydrogens
        mol = Chem.AddHs(mol)
        
        # Get charge and multiplicity 
        charge = Chem.GetFormalCharge(mol)
        num_radicals = Descriptors.NumRadicalElectrons(mol)
        multiplicity = num_radicals + 1
        # Convert to XYZ format
        xyz_str = ""
        for atom in mol.GetAtoms():
            pos = mol.GetConformer().GetAtomPosition(atom.GetIdx())
            xyz_str += "{}\t{}\t{}\t{}\n".format(atom.GetSymbol(), pos.x, pos.y, pos.z)

        return xyz_str, charge, multiplicity

def file_exists_in_subdir(subdirectory, filename):
        file_path = os.path.join(subdirectory, filename)
        return os.path.exists(file_path)