import os
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import streamlit
import matplotlib as mpl
import shap
from scipy.stats import chi2_contingency
from pycaret.clustering import *
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import pickle
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm

# 한글 폰트 경로 설정
font_path = './Custom_Fonts/NanumBarunGothic.ttf'  # 예시 경로
font_prop = fm.FontProperties(fname=font_path, size=12)

# Matplotlib 전역 설정에 폰트 적용
plt.rcParams['font.family'] = font_prop.get_name()

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

class Clustering: ############################################################################################
    def __init__(self, data, session_id=786):
        """클러스터링 클래스의 생성자입니다."""
        self.data = data
        self.session_id = session_id
        # self.models = {}
        self.clustering_model=None
        self.clustering_setup = None
        self.clustered_data = None
        self.models_dict = {}  # 모델 이름과 모델 객체를 매핑하는 딕셔너리

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
            # 상단 삼각형 마스크
            mask = np.triu(np.ones_like(corr_matrix, dtype=bool))

            # 파스텔 톤 색상 팔레트
            cmap = sns.diverging_palette(230, 20, as_cmap=True)

            plt.figure(figsize=(20, 12))
            sns.heatmap(corr_matrix, 
                        annot=True, 
                        fmt=".2f", 
                        mask = mask,
                        cmap=cmap)
            plt.title("Categorical Features Correlation Matrix", fontsize=16)
            plt.xticks(fontsize=10)
            plt.yticks(fontsize=10)
            # plt.show()
        
        except: 
            print('범주형 변수가 없습니다.')

        return plt.gcf()
    
    

    def calculate_wcss(self, range_n_clusters):
        wcss = []
        for n_clusters in range_n_clusters:
            clusterer = KMeans(n_clusters=n_clusters, random_state=42)
            clusterer.fit(self.data)
            wcss.append(clusterer.inertia_)
        return wcss

    def calculate_silhouette_scores(self, range_n_clusters):
        sil_scores = []
        for n_clusters in range_n_clusters:
            clusterer = KMeans(n_clusters=n_clusters, random_state=42)
            cluster_labels = clusterer.fit_predict(self.data)
            silhouette_avg = silhouette_score(self.data, cluster_labels)
            sil_scores.append(silhouette_avg)
        return sil_scores

    def plot_elbow_curve(self, range_n_clusters):
        wcss = self.calculate_wcss(range_n_clusters)
        plt.figure()
        plt.plot(range_n_clusters, wcss, 'bo-', markerfacecolor='red', markersize=5)
        plt.title('Elbow Curve')
        plt.xlabel('Number of clusters')
        plt.ylabel('WCSS')
        plt.grid(True)
        return plt.gcf()  # Return the figure object

    def plot_silhouette_scores(self, range_n_clusters):
        sil_scores = self.calculate_silhouette_scores(range_n_clusters)
        plt.figure()
        plt.plot(range_n_clusters, sil_scores, 'go-', markerfacecolor='red', markersize=5)
        plt.title('Silhouette Scores')
        plt.xlabel('Number of clusters')
        plt.ylabel('Silhouette Score')
        plt.grid(True)
        return plt.gcf()  # Return the figure object

    def setup(self, profile=True, session_id = 768, verbose=False):
            """클러스터링 모델을 설정합니다."""
            num_cols = self.data.select_dtypes(include=['int64', 'float64']).columns.tolist()
            cat_cols = self.data.select_dtypes(include=['object', 'category']).columns.tolist()
            date_cols = self.data.select_dtypes(include=['datetime64[ns]']).columns.tolist()

            self.clustering_setup = setup(data=self.data, 
                                          categorical_features=cat_cols,
                                          numeric_features=num_cols,
                                          date_features=date_cols,
                                          encoding_method='binary',
                                          profile=profile,
                                          verbose=verbose,
                                          session_id=session_id)
            
            result = pull()
            result = result.iloc[:-5, :]

            return self.clustering_setup, result

    def create_model(self, model_name, num_clusters=None):
        """클러스터링 모델을 생성하고 결과를 반환합니다."""
        model = create_model(model_name, num_clusters=num_clusters) if num_clusters else create_model(model_name)
        self.clustering_model = model
        self.models_dict[f"군집분석 모델"] = model
        results = pull()
        return self.models_dict, model, results

    def assign_model(self, model):
        """클러스터링 결과를 데이터에 할당합니다."""
        self.clustered_data = assign_model(model)
        result = pull()
        return self.clustered_data, result
    
    
    def save_model(self, model_name, save_directory):
        """모델을 지정된 디렉토리에 저장합니다."""
        save_path = os.path.join(save_directory, model_name)
        save_model(self.clustering_model, save_path)

    def visualize_model(self, model, plot_type):
        """
        클러스터링 모델을 시각화합니다.
        plot_type: 'cluster', 'distance', 'distribution', 'elbow', 'silhouette'
        """
        plt.figure()
        plot_result = plot_model(model, plot=plot_type, display_format='streamlit')
        return plot_result
    
    def cluster_analysis(self, df):
        """각 군집의 수치형 데이터 통계와 분포, 범주형 데이터 분포를 분석합니다."""
        cluster_descriptions = {}
        for cluster_label in list(df['Cluster'].unique()):
            cluster_data = df[df['Cluster'] == cluster_label]
            # 수치형 데이터에 대한 통계 계산
            numerical_stats = cluster_data.describe()
            # 범주형 데이터에 대한 분포 확인
            categorical_distributions = {column: cluster_data[column].value_counts() for column in cluster_data.select_dtypes(['object']).columns}
            
            # 결과를 딕셔너리에 저장
            cluster_descriptions[cluster_label] = {
                'numerical_stats': numerical_stats,
                'categorical_distributions': categorical_distributions
            }
        return cluster_descriptions
    
    def cluster_analysis_num(df, cluster_id):
        # 군집에 해당하는 데이터 필터링
        cluster_data = df[df['Cluster'] == cluster_id]
        
        # 수치형 데이터에 대한 요약 통계량 계산
        numerical_stats = cluster_data.describe()

        # 수치형 데이터 열 추출
        numerical_columns = cluster_data.select_dtypes(exclude=['object', 'category']).columns

        # 수치형 데이터가 있는 경우에만 산점도 생성
        if len(numerical_columns) > 0:
            sns.pairplot(cluster_data[numerical_columns])
            plt.suptitle(f"Scatter plot for numerical variables in Cluster {cluster_id}", fontsize=16, y=1.02)
            plt.tight_layout()
            plt.subplots_adjust(top=0.95)
            # plt.title(f"Scatter plot for numerical variables in Cluster {cluster_id}")
            return numerical_stats, plt.gcf()
        else:
            return numerical_stats, None  # 수치형 데이터가 없는 경우

    def cluster_analysis_cat(df, cluster_id):
        cluster_data = df[df['Cluster'] == cluster_id]
        categorical_columns = cluster_data.select_dtypes(include=['object', 'category']).columns

        categorical_stats = {}
        figs = {}

        for col in categorical_columns:
            value_counts = cluster_data[col].value_counts()
            categorical_stats[col] = value_counts

            # 각 범주형 변수에 대한 막대 그래프 생성
            fig, ax = plt.subplots()
            sns.barplot(x=value_counts.index, y=value_counts.values, ax=ax)
            ax.set_title(f"Distribution of {col} in Cluster {cluster_id}")
            figs[col] = fig

        return categorical_stats, figs
   

    @classmethod
    def predict_data(self, model, data):
        """모델을 사용하여 데이터를 예측합니다."""
        return predict_model(model, data=data)