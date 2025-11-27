"""
Tumor Grading System for Histopathology Analysis

Implements Nottingham grading system and related pathology assessments.
"""

from typing import Dict, Optional
import numpy as np


class TumorGradingSystem:
    """Nottingham grading system for breast cancer."""
    
    def __init__(self):
        """Initialize grading system."""
        self.nottingham_scores = {
            'tubule_formation': {
                1: '>75% of tumor area',
                2: '10-75% of tumor area',
                3: '<10% of tumor area'
            },
            'nuclear_pleomorphism': {
                1: 'Small, uniform cells',
                2: 'Moderate variation',
                3: 'Marked variation'
            },
            'mitotic_count': {
                1: '0-9 per 10 HPF',
                2: '10-19 per 10 HPF',
                3: '≥20 per 10 HPF'
            }
        }
    
    def calculate_nottingham_grade(self, tubule_score: int, nuclear_score: int, 
                                   mitotic_score: int) -> Dict:
        """
        Calculate Nottingham grade from component scores.
        
        Args:
            tubule_score: Tubule formation score (1-3)
            nuclear_score: Nuclear pleomorphism score (1-3)
            mitotic_score: Mitotic count score (1-3)
            
        Returns:
            Complete grading information
        """
        total_score = tubule_score + nuclear_score + mitotic_score
        
        # Determine grade
        if total_score <= 5:
            grade = 1
            grade_name = "Grade 1 (Well Differentiated)"
        elif total_score <= 7:
            grade = 2
            grade_name = "Grade 2 (Moderately Differentiated)"
        else:
            grade = 3
            grade_name = "Grade 3 (Poorly Differentiated)"
        
        return {
            'nottingham_score': total_score,
            'grade': grade,
            'grade_name': grade_name,
            'component_scores': {
                'tubule_formation': tubule_score,
                'nuclear_pleomorphism': nuclear_score,
                'mitotic_count': mitotic_score
            },
            'interpretation': self._get_grade_interpretation(grade),
            'prognostic_significance': self._get_prognostic_info(grade)
        }
    
    def estimate_mitotic_count(self, image_features: Dict) -> Dict:
        """
        Estimate mitotic count from image features.
        
        Args:
            image_features: Extracted image features
            
        Returns:
            Mitotic count estimation
        """
        # Simplified estimation based on image features
        # In production, this would use deep learning models
        
        cell_density = image_features.get('cell_density', 0)
        nuclear_features = image_features.get('nuclear_features', {})
        
        # Estimate mitoses per 10 HPF (high power fields)
        estimated_mitoses = cell_density * 0.1  # Simplified calculation
        
        # Determine score
        if estimated_mitoses < 10:
            mitotic_score = 1
        elif estimated_mitoses < 20:
            mitotic_score = 2
        else:
            mitotic_score = 3
        
        return {
            'estimated_mitoses_per_10_hpf': round(estimated_mitoses, 1),
            'mitotic_score': mitotic_score,
            'confidence': 'moderate',  # Would be calculated from model confidence
            'interpretation': self._interpret_mitotic_count(estimated_mitoses)
        }
    
    def estimate_ki67_index(self, image_features: Dict) -> Dict:
        """
        Estimate Ki-67 proliferation index.
        
        Args:
            image_features: Image features
            
        Returns:
            Ki-67 estimation
        """
        # Simplified estimation
        proliferation_markers = image_features.get('proliferation_markers', 0)
        
        # Estimate Ki-67 percentage
        ki67_percentage = min(100, proliferation_markers * 10)
        
        # Classify
        if ki67_percentage < 14:
            category = "Low"
            interpretation = "Low proliferation rate"
        elif ki67_percentage < 30:
            category = "Intermediate"
            interpretation = "Moderate proliferation rate"
        else:
            category = "High"
            interpretation = "High proliferation rate"
        
        return {
            'ki67_percentage': round(ki67_percentage, 1),
            'category': category,
            'interpretation': interpretation,
            'clinical_significance': self._get_ki67_significance(ki67_percentage)
        }
    
    def _get_grade_interpretation(self, grade: int) -> str:
        """Get interpretation of grade."""
        interpretations = {
            1: "Well-differentiated tumor with good prognosis",
            2: "Moderately differentiated tumor with intermediate prognosis",
            3: "Poorly differentiated tumor with more aggressive behavior"
        }
        return interpretations.get(grade, "Unknown")
    
    def _get_prognostic_info(self, grade: int) -> Dict:
        """Get prognostic information."""
        prognostic_data = {
            1: {
                'recurrence_risk': 'Low',
                'survival_rate': 'High',
                'treatment_aggressiveness': 'Standard'
            },
            2: {
                'recurrence_risk': 'Moderate',
                'survival_rate': 'Moderate',
                'treatment_aggressiveness': 'Standard to Aggressive'
            },
            3: {
                'recurrence_risk': 'High',
                'survival_rate': 'Lower',
                'treatment_aggressiveness': 'Aggressive'
            }
        }
        return prognostic_data.get(grade, {})
    
    def _interpret_mitotic_count(self, count: float) -> str:
        """Interpret mitotic count."""
        if count < 10:
            return "Low mitotic activity - favorable"
        elif count < 20:
            return "Moderate mitotic activity"
        else:
            return "High mitotic activity - aggressive tumor"
    
    def _get_ki67_significance(self, percentage: float) -> str:
        """Get clinical significance of Ki-67."""
        if percentage < 14:
            return "May benefit from endocrine therapy"
        elif percentage >= 30:
            return "May benefit from chemotherapy"
        else:
            return "Consider both endocrine and chemotherapy"


class StagingSupport:
    """Support for TNM staging."""
    
    @staticmethod
    def calculate_tnm_stage(t_stage: str, n_stage: str, m_stage: str, 
                           grade: int, er_status: bool, pr_status: bool, 
                           her2_status: bool) -> Dict:
        """
        Calculate TNM stage and stage group.
        
        Args:
            t_stage: Tumor size stage (T1-T4)
            n_stage: Node stage (N0-N3)
            m_stage: Metastasis stage (M0-M1)
            grade: Tumor grade (1-3)
            er_status: Estrogen receptor status
            pr_status: Progesterone receptor status
            her2_status: HER2 status
            
        Returns:
            Complete staging information
        """
        # Determine stage group (simplified)
        if m_stage == 'M1':
            stage_group = 'IV'
        elif t_stage in ['T1', 'T2'] and n_stage == 'N0':
            stage_group = 'I' if t_stage == 'T1' else 'IIA'
        elif t_stage == 'T3' or n_stage in ['N1', 'N2']:
            stage_group = 'IIB' if n_stage == 'N0' else 'IIIA'
        else:
            stage_group = 'IIIB'
        
        # Molecular subtype
        subtype = StagingSupport._determine_molecular_subtype(
            er_status, pr_status, her2_status
        )
        
        return {
            'tnm_stage': f"{t_stage}{n_stage}{m_stage}",
            'stage_group': stage_group,
            'molecular_subtype': subtype,
            'grade': grade,
            'receptor_status': {
                'ER': 'Positive' if er_status else 'Negative',
                'PR': 'Positive' if pr_status else 'Negative',
                'HER2': 'Positive' if her2_status else 'Negative'
            },
            'prognostic_factors': StagingSupport._get_prognostic_factors(
                stage_group, grade, subtype
            )
        }
    
    @staticmethod
    def _determine_molecular_subtype(er: bool, pr: bool, her2: bool) -> str:
        """Determine molecular subtype."""
        if er or pr:
            if her2:
                return "HER2-positive"
            else:
                return "Luminal"
        elif her2:
            return "HER2-enriched"
        else:
            return "Triple-negative"
    
    @staticmethod
    def _get_prognostic_factors(stage: str, grade: int, subtype: str) -> Dict:
        """Get prognostic factors."""
        return {
            'stage_prognosis': 'Favorable' if stage in ['I', 'IIA'] else 'Moderate' if stage == 'IIB' else 'Unfavorable',
            'grade_prognosis': 'Favorable' if grade == 1 else 'Moderate' if grade == 2 else 'Unfavorable',
            'subtype_prognosis': 'Favorable' if subtype == 'Luminal' else 'Moderate' if subtype == 'HER2-positive' else 'Unfavorable'
        }

