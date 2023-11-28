from pydantic import BaseModel, validator


class PredictionRow(BaseModel):
    Mean_of_the_integrated_profile: float 
    Standard_deviation_of_the_integrated_profile: float 
    Excess_kurtosis_of_the_integrated_profile: float 
    Skewness_of_the_integrated_profile: float 
    Mean_of_the_DM_SNR_curve: float 
    Standard_deviation_of_the_DM_SNR_curve: float 
    Excess_kurtosis_of_the_DM_SNR_curve: float 
    Skewness_of_the_DM_SNR_curve: float

    @validator('Mean_of_the_integrated_profile')
    def mean_of_integrated_profile_check(cls, v):
        if v >= 0 and v <= 200:
            return v
        raise ValueError('Mean_of_the_integrated_profile must be between 0 and 200')

    @validator('Standard_deviation_of_the_integrated_profile')
    def std_dev_of_integrated_profile_check(cls, v):
        if v >= 0 and v <= 100:
            return v
        raise ValueError('Standard_deviation_of_the_integrated_profile must be between 0 and 100')

    @validator('Excess_kurtosis_of_the_integrated_profile')
    def excess_kurtosis_of_integrated_profile_check(cls, v):
        if v >= -10 and v <= 10:
            return v
        raise ValueError('Excess_kurtosis_of_the_integrated_profile must be between -10 and 10')

    @validator('Skewness_of_the_integrated_profile')
    def skewness_of_integrated_profile_check(cls, v):
        if v >= -10 and v <= 100:
            return v
        raise ValueError('Skewness_of_the_integrated_profile must be between -10 and 100')

    @validator('Mean_of_the_DM_SNR_curve')
    def mean_of_DM_SNR_curve_check(cls, v):
        if v >= 0 and v <= 300:
            return v
        raise ValueError('Mean_of_the_DM_SNR_curve must be between 0 and 300')

    @validator('Standard_deviation_of_the_DM_SNR_curve')
    def std_dev_of_DM_SNR_curve_check(cls, v):
        if v >= 0 and v <= 150:
            return v
        raise ValueError('Standard_deviation_of_the_DM_SNR_curve must be between 0 and 100')

    @validator('Excess_kurtosis_of_the_DM_SNR_curve')
    def excess_kurtosis_of_DM_SNR_curve_check(cls, v):
        if v >= -10 and v <= 100:
            return v
        raise ValueError('Excess_kurtosis_of_the_DM_SNR_curve must be between -10 and 100')

    @validator('Skewness_of_the_DM_SNR_curve')
    def skewness_of_DM_SNR_curve_check(cls, v):
        if v >= -10 and v <= 10:
            return v
        raise ValueError('Skewness_of_the_DM_SNR_curve must be between -10 and 10')
