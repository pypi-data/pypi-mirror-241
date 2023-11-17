import os
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit
import matplotlib as mpl
import shap
from scipy.stats import chi2_contingency
from pycaret.anomaly import *
import pickle

# -*- coding: utf-8-sig -*-

# 폰트 설정
# font_path = '/Users/yerin/Library/Fonts/NanumBarunGothic.ttf'
# font_name = plt.matplotlib.font_manager.FontProperties(fname=font_path).get_name()
# plt.rcParams['font.family'] = font_name
# # font = fm.FontProperties(fname=fontpath, size = 24)

def cramers_v(x, y):
    """Cramér's V를 계산합니다."""
    confusion_matrix = pd.crosstab(x, y)
    chi2 = chi2_contingency(confusion_matrix)[0]
    n = confusion_matrix.sum().sum()
    phi2 = chi2 / n
    r, k = confusion_matrix.shape
    phi2corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    rcorr = r - ((r - 1) ** 2) / (n - 1)
    kcorr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2corr / min((kcorr - 1), (rcorr - 1)))

class AnomalyDetection:
    def __init__(self, data, target_column):
        """이상치 탐지 클래스의 생성자입니다."""
        self.data = data
        self.models = ['iforest', 'knn', 'lof', 'pca']
        self.models_dict = {}  # 모델 이름과 모델 객체를 매핑하는 딕셔너리
        self.results = {}
        
        # self.optimization_completed = False  # 상태 추적 변수 추가

    # 데이터 불러오기
    def load_data(self):
        """데이터를 불러옵니다."""
        if self.data_path.endswith('.csv'):
            self.data = pd.read_csv(self.data_path, encoding='utf-8-sig')
        elif self.data_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.data_path)
        elif self.data_path.endswith(('.pkl', '.pickle')):
            with open(self.data_path, 'rb') as file:
                self.data = pickle.load(file)
        # 추가적인 데이터 형식에 대한 처리 (예: .xlsx)는 필요에 따라 확장 가능

    def load_data(self, dataframe=None):
        """데이터를 불러옵니다. 파일 경로 또는 데이터프레임을 사용합니다."""
        if dataframe is not None:
            self.data = dataframe
        elif self.data_path.endswith('.csv'):
            self.data = pd.read_csv(self.data_path, encoding='utf-8-sig')
        elif self.data_path.endswith('.xlsx'):
            self.data = pd.read_excel(self.data_path)
        elif self.data_path.endswith(('.pkl', '.pickle')):
            with open(self.data_path, 'rb') as file:
                self.data = pickle.load(file)
        
    def load_uploaded_file(uploaded_file):
        if uploaded_file.name.endswith('.csv'):
            return pd.read_csv(uploaded_file)
        elif uploaded_file.name.endswith('.xlsx'):
            return pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith(('.pkl', '.pickle')):
            return pickle.load(uploaded_file)

    # 데이터 탐색
    def explore_data(self):
        """데이터의 형태와 컬럼을 확인합니다."""
        print(f'데이터 행 수: {self.data.shape[0]}')
        print(f'데이터 열 수: {self.data.shape[1]}')
        print(f'데이터 컬럼: {self.data.columns}')
        data_description = self.data.describe()
        return data_description
        
    # 타입 별 변수 구분
    def feature_type(self):
        """데이터의 변수 타입을 구분합니다."""
        categorical_features = self.data.select_dtypes(include=['object']).columns.tolist()
        numerical_features = self.data.select_dtypes(exclude=['object']).columns.tolist()
        print(f'Categorical Features: {categorical_features}')
        print(f'Numerical Features: {numerical_features}')
        return categorical_features, numerical_features

    # 수치형 변수 시각화
    def visualize_numerical_distribution(self):
        """수치형 변수의 분포를 시각화합니다."""
        
        # 수치형 변수 추출
        num_cols = self.data.select_dtypes(exclude=['object']).columns.tolist()
        
        # 그래프 스타일 및 팔레트 설정
        sns.set_style("whitegrid")
        sns.set_palette("pastel")

        # 그래프의 행과 열 수 계산 (2개의 열)
        rows = len(num_cols) // 2
        if len(num_cols) % 2:
            rows += 1

        # 그래프 크기와 간격 조정
        fig, axes = plt.subplots(rows, 2, figsize=(14, 5 * rows))
        for i, column in enumerate(num_cols):
            ax = axes[i // 2, i % 2] if rows > 1 else axes[i % 2]
            sns.histplot(self.data[column], kde=True, bins=30, ax=ax)
            ax.set_title(f'Distribution of {column}', fontsize=15)
            ax.set_ylabel('Frequency')

        # 불필요한 빈 서브플롯 제거
        if len(num_cols) % 2:
            if rows > 1:
                axes[-1, -1].axis('off')
            else:
                axes[-1].axis('off')

        # 간격 조정
        plt.tight_layout()
        return plt.gcf()

    # 범주형 변수 시각화
    def visualize_categorical_distribution(self):
        """범주형 변수의 분포를 시각화합니다."""
        # 범주형 변수 추출
        cat_cols = self.data.select_dtypes(include=['object']).columns.tolist()
        
        # 범주형 변수가 없으면 None 반환
        if not cat_cols:
            print('범주형 변수가 없습니다.')
            return None

        # 그래프 그리기 설정
        rows = len(cat_cols)

        # 시각화 설정
        sns.set_style("whitegrid")
        palette = sns.color_palette("pastel")

        # 범주형 변수의 분포와 빈도를 시각화
        fig, axes = plt.subplots(rows, 1, figsize=(10, 5 * rows), squeeze=False)
        for i, column in enumerate(cat_cols):
            sns.countplot(y=self.data[column], ax=axes[i, 0], palette=palette, order=self.data[column].value_counts().index)
            axes[i, 0].set_title(f'Distribution of {column}')
            axes[i, 0].set_xlabel('Count')

        plt.tight_layout()
        return fig
        

    # 결측치 시각화
    def visualize_missing_distribution(self):
        """결측치 분포를 시각화합니다."""
        
        # 결측치 비율 계산
        missing_ratio = self.data.isnull().mean() * 100
        missing_count = self.data.isnull().sum()

        # 결측치 건수 및 비율에 대한 데이터프레임
        missing_df = pd.DataFrame({'Missing Count': missing_count, 'Missing Ratio (%)': missing_ratio})

        # 결측치 비율을 시각화
        plt.figure(figsize=(16, 8))
        sns.barplot(x=missing_ratio.index, y=missing_ratio, palette=sns.color_palette("pastel"))
        plt.axhline(30, color='red', linestyle='--')  # 30% 초과를 나타내는 빨간색 점선 추가
        plt.xticks(rotation=45)
        plt.title('Percentage of Missing Values by Columns')
        plt.ylabel('Missing Value Percentage (%)')
        plt.tight_layout()

        # plt.show()
        return missing_df, plt.gcf()

    # 결측치 처리
    def handle_and_visualize_missing(self, threshold=30):
        """결측치 처리 후 데이터를 확인하고 시각화합니다."""
        
        # 1. 결측치 비율 계산
        missing_ratio = self.data.isnull().mean() * 100
        
        # 2. 결측치 비율이 threshold(기본값: 30%)가 넘는 변수들 추출
        columns_to_drop = missing_ratio[missing_ratio > threshold].index.tolist()

        # 3. 해당 변수들 제거
        self.data.drop(columns=columns_to_drop, inplace=True)

        # 4. 결측치 비율 재확인
        missing_ratio_cleaned = self.data.isnull().mean() * 100
        missing_count_cleaned = self.data.isnull().sum()

        # 결측치 건수 및 비율에 대한 데이터프레임
        missing_df_cleaned = pd.DataFrame({'Missing Count': missing_count_cleaned, 'Missing Ratio (%)': missing_ratio_cleaned})

        # 시각화 그래프
        plt.figure(figsize=(16, 8))
        sns.barplot(x=missing_ratio_cleaned.index, y=missing_ratio_cleaned, palette=sns.color_palette("pastel"))
        plt.ylim(0, 100) # y축의 범위를 0부터 100까지로 설정
        plt.xticks(rotation=45)
        plt.title('Percentage of Missing Values by Columns (After Cleaning)')
        plt.ylabel('Missing Value Percentage (%)')
        plt.tight_layout()

        # plt.show()
        return missing_df_cleaned, plt.gcf()

    # 수치형 상관관계 분석
    def numerical_correlation(self):
        """수치형 변수들 간의 상관관계를 분석합니다."""
        corr_matrix = self.data.corr()

        # 상단 삼각형 마스크
        mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

        # 파스텔 톤 색상 팔레트
        cmap = sns.diverging_palette(230, 20, as_cmap=True)

        plt.figure(figsize=(20, 12))
        sns.heatmap(corr_matrix, 
                    annot=True, 
                    fmt=".2f", 
                    cmap=cmap, 
                    mask=mask,
                    linewidths=0.5,
                    cbar_kws={"shrink": .8})
        plt.title("Numerical Features Correlation Matrix", fontsize=16)
        plt.xticks(fontsize=10)
        plt.yticks(fontsize=10)
        # plt.show()
        return plt.gcf()
    
    def categorical_correlation(self):
        """범주형 변수들 간의 상관관계를 분석합니다."""
        try:
            columns = self.data.select_dtypes(include=['object', 'category']).columns
            corr_matrix = pd.DataFrame(index=columns, columns=columns)

            for i in columns:
                for j in columns:
                    corr_matrix.loc[i, j] = cramers_v(self.data[i], self.data[j])

            corr_matrix = corr_matrix.astype(float)

            # 파스텔 톤 색상 팔레트
            cmap = sns.diverging_palette(230, 20, as_cmap=True)

            plt.figure(figsize=(20, 12))
            sns.heatmap(corr_matrix, 
                        annot=True, 
                        fmt=".2f", 
                        cmap=cmap)
            plt.title("Categorical Features Correlation Matrix", fontsize=16)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            # plt.show()
        
        except: 
            print('범주형 변수가 없습니다.')

        return plt.gcf()
        
    # 옵션 설정
    def setup(self, session_id = 786, normalize = True, normalize_method = 'zscore', profile = True):
        """이상치 탐지 모델을 설정합니다."""
        num_cols = self.data.select_dtypes(include=['int64', 'float64']).columns.tolist()
        cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
        date_cols = self.data.select_dtypes(include=['datetime64[ns]']).columns.tolist()
                                
        self.setup_data = setup(data=self.data,
                                categorical_features=cat_cols,
                                numeric_features=num_cols,
                                date_features=date_cols,
                                encoding_method='binary',
                                session_id=session_id,
                                normalize=normalize,
                                normalize_method=normalize_method
                                )
        
        result = pull()
        result = result.iloc[:-5, :]

        return self.setup_data, result

    # 모델 생성
    def create_models(self):
        self.models_dict = {}
        for model_name in self.models:
            model = create_model(model_name)
            self.anomaly_model = model
            assigned_data = assign_model(model)
            self.models_dict[model_name] = model
            self.results[model_name] = assigned_data

    def get_models(self):
        return self.models_dict
    
    def get_results(self):
        return self.results
    
    def save_model(self, model_name, selected_model, save_directory):
        """모델을 지정된 디렉토리에 저장합니다."""
        save_path = os.path.join(save_directory, model_name)
        save_model(selected_model, save_path)
        
    # 모델 시각화
    def visualize_model(self, model, plot_type):
        """
        선택된 모델의 성능을 시각화합니다.
        plot_type: 'tsne', 'umap'
        """
        plot_result = plot_model(model, plot=plot_type, display_format='streamlit')
        return plot_result   

    @classmethod
    def predict_data(cls, model, data):
        """모델을 사용하여 데이터를 예측합니다."""
        predictions = predict_model(model, data=data)
        return predictions