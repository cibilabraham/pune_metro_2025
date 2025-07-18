PGDMP     '        
            }            asset-optima_update1    14.1    14.1 R   �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    57876    asset-optima_update1    DATABASE     z   CREATE DATABASE "asset-optima_update1" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
 &   DROP DATABASE "asset-optima_update1";
                postgres    false            �            1259    57877 $   admin_tools_stats_criteriatostatsm2m    TABLE     [  CREATE TABLE public.admin_tools_stats_criteriatostatsm2m (
    id integer NOT NULL,
    "order" integer,
    prefix character varying(255) NOT NULL,
    use_as character varying(90) NOT NULL,
    criteria_id integer NOT NULL,
    stats_id integer NOT NULL,
    CONSTRAINT admin_tools_stats_criteriatostatsm2m_order_check CHECK (("order" >= 0))
);
 8   DROP TABLE public.admin_tools_stats_criteriatostatsm2m;
       public         heap    postgres    false            �            1259    57881 +   admin_tools_stats_criteriatostatsm2m_id_seq    SEQUENCE     �   CREATE SEQUENCE public.admin_tools_stats_criteriatostatsm2m_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 B   DROP SEQUENCE public.admin_tools_stats_criteriatostatsm2m_id_seq;
       public          postgres    false    209            �           0    0 +   admin_tools_stats_criteriatostatsm2m_id_seq    SEQUENCE OWNED BY     {   ALTER SEQUENCE public.admin_tools_stats_criteriatostatsm2m_id_seq OWNED BY public.admin_tools_stats_criteriatostatsm2m.id;
          public          postgres    false    210            �            1259    57882 
   auth_group    TABLE     f   CREATE TABLE public.auth_group (
    id integer NOT NULL,
    name character varying(150) NOT NULL
);
    DROP TABLE public.auth_group;
       public         heap    postgres    false            �            1259    57885    auth_group_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 (   DROP SEQUENCE public.auth_group_id_seq;
       public          postgres    false    211            �           0    0    auth_group_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.auth_group_id_seq OWNED BY public.auth_group.id;
          public          postgres    false    212            �            1259    57886    auth_group_permissions    TABLE     �   CREATE TABLE public.auth_group_permissions (
    id integer NOT NULL,
    group_id integer NOT NULL,
    permission_id integer NOT NULL
);
 *   DROP TABLE public.auth_group_permissions;
       public         heap    postgres    false            �            1259    57889    auth_group_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_group_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.auth_group_permissions_id_seq;
       public          postgres    false    213            �           0    0    auth_group_permissions_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.auth_group_permissions_id_seq OWNED BY public.auth_group_permissions.id;
          public          postgres    false    214            �            1259    57890    auth_permission    TABLE     �   CREATE TABLE public.auth_permission (
    id integer NOT NULL,
    name character varying(255) NOT NULL,
    content_type_id integer NOT NULL,
    codename character varying(100) NOT NULL
);
 #   DROP TABLE public.auth_permission;
       public         heap    postgres    false            �            1259    57893    auth_permission_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_permission_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.auth_permission_id_seq;
       public          postgres    false    215            �           0    0    auth_permission_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.auth_permission_id_seq OWNED BY public.auth_permission.id;
          public          postgres    false    216            �            1259    57894 	   auth_user    TABLE       CREATE TABLE public.auth_user (
    id integer NOT NULL,
    password character varying(128) NOT NULL,
    last_login timestamp with time zone,
    is_superuser boolean NOT NULL,
    username character varying(150) NOT NULL,
    first_name character varying(150) NOT NULL,
    last_name character varying(150) NOT NULL,
    email character varying(254) NOT NULL,
    is_staff boolean NOT NULL,
    is_active boolean NOT NULL,
    date_joined timestamp with time zone NOT NULL,
    role integer DEFAULT 0 NOT NULL
);
    DROP TABLE public.auth_user;
       public         heap    postgres    false            �           0    0    COLUMN auth_user.role    COMMENT     8   COMMENT ON COLUMN public.auth_user.role IS 'user role';
          public          postgres    false    217            �            1259    57900    auth_user_groups    TABLE        CREATE TABLE public.auth_user_groups (
    id integer NOT NULL,
    user_id integer NOT NULL,
    group_id integer NOT NULL
);
 $   DROP TABLE public.auth_user_groups;
       public         heap    postgres    false            �            1259    57903    auth_user_groups_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_groups_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.auth_user_groups_id_seq;
       public          postgres    false    218            �           0    0    auth_user_groups_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.auth_user_groups_id_seq OWNED BY public.auth_user_groups.id;
          public          postgres    false    219            �            1259    57904    auth_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.auth_user_id_seq;
       public          postgres    false    217            �           0    0    auth_user_id_seq    SEQUENCE OWNED BY     E   ALTER SEQUENCE public.auth_user_id_seq OWNED BY public.auth_user.id;
          public          postgres    false    220            �            1259    57905    auth_user_user_permissions    TABLE     �   CREATE TABLE public.auth_user_user_permissions (
    id integer NOT NULL,
    user_id integer NOT NULL,
    permission_id integer NOT NULL
);
 .   DROP TABLE public.auth_user_user_permissions;
       public         heap    postgres    false            �            1259    57908 !   auth_user_user_permissions_id_seq    SEQUENCE     �   CREATE SEQUENCE public.auth_user_user_permissions_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 8   DROP SEQUENCE public.auth_user_user_permissions_id_seq;
       public          postgres    false    221            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE OWNED BY     g   ALTER SEQUENCE public.auth_user_user_permissions_id_seq OWNED BY public.auth_user_user_permissions.id;
          public          postgres    false    222            �            1259    57909    dash_stats_criteria    TABLE     Z  CREATE TABLE public.dash_stats_criteria (
    id integer NOT NULL,
    criteria_name character varying(90) NOT NULL,
    criteria_fix_mapping jsonb,
    dynamic_criteria_field_name character varying(90),
    criteria_dynamic_mapping jsonb,
    created_date timestamp with time zone NOT NULL,
    updated_date timestamp with time zone NOT NULL
);
 '   DROP TABLE public.dash_stats_criteria;
       public         heap    postgres    false            �            1259    57914    dash_stats_criteria_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dash_stats_criteria_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.dash_stats_criteria_id_seq;
       public          postgres    false    223            �           0    0    dash_stats_criteria_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.dash_stats_criteria_id_seq OWNED BY public.dash_stats_criteria.id;
          public          postgres    false    224            �            1259    57915    dashboard_stats    TABLE     �  CREATE TABLE public.dashboard_stats (
    id integer NOT NULL,
    graph_key character varying(90) NOT NULL,
    graph_title character varying(90) NOT NULL,
    model_app_name character varying(90) NOT NULL,
    model_name character varying(90) NOT NULL,
    date_field_name character varying(90) NOT NULL,
    operation_field_name character varying(90),
    type_operation_field_name character varying(90),
    is_visible boolean NOT NULL,
    created_date timestamp with time zone NOT NULL,
    updated_date timestamp with time zone NOT NULL,
    user_field_name character varying(90),
    default_chart_type character varying(90) NOT NULL,
    default_time_period integer NOT NULL,
    default_time_scale character varying(90) NOT NULL,
    y_axis_format character varying(90),
    "distinct" boolean NOT NULL,
    CONSTRAINT dashboard_stats_default_time_period_check CHECK ((default_time_period >= 0))
);
 #   DROP TABLE public.dashboard_stats;
       public         heap    postgres    false            �            1259    57921    dashboard_stats_id_seq    SEQUENCE     �   CREATE SEQUENCE public.dashboard_stats_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 -   DROP SEQUENCE public.dashboard_stats_id_seq;
       public          postgres    false    225            �           0    0    dashboard_stats_id_seq    SEQUENCE OWNED BY     Q   ALTER SEQUENCE public.dashboard_stats_id_seq OWNED BY public.dashboard_stats.id;
          public          postgres    false    226            �            1259    57922    django_admin_log    TABLE     �  CREATE TABLE public.django_admin_log (
    id integer NOT NULL,
    action_time timestamp with time zone NOT NULL,
    object_id text,
    object_repr character varying(200) NOT NULL,
    action_flag smallint NOT NULL,
    change_message text NOT NULL,
    content_type_id integer,
    user_id integer NOT NULL,
    CONSTRAINT django_admin_log_action_flag_check CHECK ((action_flag >= 0))
);
 $   DROP TABLE public.django_admin_log;
       public         heap    postgres    false            �            1259    57928    django_admin_log_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_admin_log_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.django_admin_log_id_seq;
       public          postgres    false    227            �           0    0    django_admin_log_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.django_admin_log_id_seq OWNED BY public.django_admin_log.id;
          public          postgres    false    228            �            1259    57929    django_content_type    TABLE     �   CREATE TABLE public.django_content_type (
    id integer NOT NULL,
    app_label character varying(100) NOT NULL,
    model character varying(100) NOT NULL
);
 '   DROP TABLE public.django_content_type;
       public         heap    postgres    false            �            1259    57932    django_content_type_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_content_type_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 1   DROP SEQUENCE public.django_content_type_id_seq;
       public          postgres    false    229            �           0    0    django_content_type_id_seq    SEQUENCE OWNED BY     Y   ALTER SEQUENCE public.django_content_type_id_seq OWNED BY public.django_content_type.id;
          public          postgres    false    230            �            1259    57933    django_migrations    TABLE     �   CREATE TABLE public.django_migrations (
    id integer NOT NULL,
    app character varying(255) NOT NULL,
    name character varying(255) NOT NULL,
    applied timestamp with time zone NOT NULL
);
 %   DROP TABLE public.django_migrations;
       public         heap    postgres    false            �            1259    57938    django_migrations_id_seq    SEQUENCE     �   CREATE SEQUENCE public.django_migrations_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public.django_migrations_id_seq;
       public          postgres    false    231            �           0    0    django_migrations_id_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public.django_migrations_id_seq OWNED BY public.django_migrations.id;
          public          postgres    false    232            �            1259    57939    django_session    TABLE     �   CREATE TABLE public.django_session (
    session_key character varying(40) NOT NULL,
    session_data text NOT NULL,
    expire_date timestamp with time zone NOT NULL
);
 "   DROP TABLE public.django_session;
       public         heap    postgres    false            �            1259    57944    fracas_action    TABLE     B  CREATE TABLE public.fracas_action (
    action_id integer NOT NULL,
    action_description character varying(550) NOT NULL,
    action_owner character varying(550) NOT NULL,
    action_status character varying(550) NOT NULL,
    action_due_date date,
    progress_log text NOT NULL,
    defect_discussion_id_id integer
);
 !   DROP TABLE public.fracas_action;
       public         heap    postgres    false            �            1259    57949    fracas_action_action_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_action_action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.fracas_action_action_id_seq;
       public          postgres    false    234            �           0    0    fracas_action_action_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.fracas_action_action_id_seq OWNED BY public.fracas_action.action_id;
          public          postgres    false    235            �            1259    57950    fracas_asset    TABLE       CREATE TABLE public.fracas_asset (
    id integer NOT NULL,
    asset_config_id character varying(550) NOT NULL,
    location_id text NOT NULL,
    location_description text NOT NULL,
    asset_serial_number character varying(550) NOT NULL,
    asset_type integer NOT NULL,
    asset_description text NOT NULL,
    software_version character varying(550) NOT NULL,
    software_description text NOT NULL,
    asset_status character varying(550) NOT NULL,
    is_active integer NOT NULL,
    "P_id" integer NOT NULL
);
     DROP TABLE public.fracas_asset;
       public         heap    postgres    false            �            1259    57955    fracas_asset_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_asset_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 *   DROP SEQUENCE public.fracas_asset_id_seq;
       public          postgres    false    236            �           0    0    fracas_asset_id_seq    SEQUENCE OWNED BY     K   ALTER SEQUENCE public.fracas_asset_id_seq OWNED BY public.fracas_asset.id;
          public          postgres    false    237            �            1259    57956    fracas_assetregister    TABLE     F   CREATE TABLE public.fracas_assetregister (
    id integer NOT NULL
);
 (   DROP TABLE public.fracas_assetregister;
       public         heap    postgres    false            �            1259    57959    fracas_assetregister_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_assetregister_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.fracas_assetregister_id_seq;
       public          postgres    false    238            �           0    0    fracas_assetregister_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.fracas_assetregister_id_seq OWNED BY public.fracas_assetregister.id;
          public          postgres    false    239            �            1259    57960    fracas_correctiveaction    TABLE     �  CREATE TABLE public.fracas_correctiveaction (
    corrective_action_id integer NOT NULL,
    corrective_action_owner character varying(550) NOT NULL,
    corrective_action_description text NOT NULL,
    corrective_action_update text NOT NULL,
    corrective_action_status character varying(550) NOT NULL,
    defect_id integer NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 +   DROP TABLE public.fracas_correctiveaction;
       public         heap    postgres    false            �            1259    57965 0   fracas_correctiveaction_corrective_action_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_correctiveaction_corrective_action_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 G   DROP SEQUENCE public.fracas_correctiveaction_corrective_action_id_seq;
       public          postgres    false    240            �           0    0 0   fracas_correctiveaction_corrective_action_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public.fracas_correctiveaction_corrective_action_id_seq OWNED BY public.fracas_correctiveaction.corrective_action_id;
          public          postgres    false    241            �            1259    57966    fracas_defect    TABLE     �  CREATE TABLE public.fracas_defect (
    start_date date,
    end_date date,
    asset_type character varying(550) NOT NULL,
    defect_id integer NOT NULL,
    defect_description text NOT NULL,
    defect_open_date date,
    defect_closed_date date,
    investigation text NOT NULL,
    defect_status character varying(550) NOT NULL,
    defect_status_remarks text NOT NULL,
    oem_defect_reference text NOT NULL,
    oem_target_date date,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 !   DROP TABLE public.fracas_defect;
       public         heap    postgres    false            �            1259    57971    fracas_defect_defect_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_defect_defect_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public.fracas_defect_defect_id_seq;
       public          postgres    false    242            �           0    0    fracas_defect_defect_id_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public.fracas_defect_defect_id_seq OWNED BY public.fracas_defect.defect_id;
          public          postgres    false    243            �            1259    57972    fracas_defectdiscussion    TABLE     �   CREATE TABLE public.fracas_defectdiscussion (
    defect_discussion_id integer NOT NULL,
    meeting_date date,
    defect_id integer,
    review_board_id integer NOT NULL,
    description character varying(550) NOT NULL
);
 +   DROP TABLE public.fracas_defectdiscussion;
       public         heap    postgres    false            �            1259    57977 !   fracas_defectdiscussion_attendees    TABLE     �   CREATE TABLE public.fracas_defectdiscussion_attendees (
    id integer NOT NULL,
    defectdiscussion_id integer NOT NULL,
    userprofile_id integer NOT NULL
);
 5   DROP TABLE public.fracas_defectdiscussion_attendees;
       public         heap    postgres    false            �            1259    57980 (   fracas_defectdiscussion_attendees_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_defectdiscussion_attendees_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ?   DROP SEQUENCE public.fracas_defectdiscussion_attendees_id_seq;
       public          postgres    false    245            �           0    0 (   fracas_defectdiscussion_attendees_id_seq    SEQUENCE OWNED BY     u   ALTER SEQUENCE public.fracas_defectdiscussion_attendees_id_seq OWNED BY public.fracas_defectdiscussion_attendees.id;
          public          postgres    false    246            �            1259    57981 0   fracas_defectdiscussion_defect_discussion_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_defectdiscussion_defect_discussion_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 G   DROP SEQUENCE public.fracas_defectdiscussion_defect_discussion_id_seq;
       public          postgres    false    244            �           0    0 0   fracas_defectdiscussion_defect_discussion_id_seq    SEQUENCE OWNED BY     �   ALTER SEQUENCE public.fracas_defectdiscussion_defect_discussion_id_seq OWNED BY public.fracas_defectdiscussion.defect_discussion_id;
          public          postgres    false    247            �            1259    57982    fracas_employeemaster    TABLE     �   CREATE TABLE public.fracas_employeemaster (
    id integer NOT NULL,
    employee_id character varying(550),
    name character varying(550) NOT NULL,
    designation character varying(550) NOT NULL
);
 )   DROP TABLE public.fracas_employeemaster;
       public         heap    postgres    false            �            1259    57987    fracas_employeemaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_employeemaster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 3   DROP SEQUENCE public.fracas_employeemaster_id_seq;
       public          postgres    false    248            �           0    0    fracas_employeemaster_id_seq    SEQUENCE OWNED BY     ]   ALTER SEQUENCE public.fracas_employeemaster_id_seq OWNED BY public.fracas_employeemaster.id;
          public          postgres    false    249            �            1259    57988    fracas_failuredata    TABLE     	  CREATE TABLE public.fracas_failuredata (
    id integer NOT NULL,
    failure_id character varying(600),
    event_description character varying(600) NOT NULL,
    date date NOT NULL,
    "time" time without time zone NOT NULL,
    detection character varying(600) NOT NULL,
    service_delay character varying(600),
    immediate_investigation text NOT NULL,
    failure_type character varying(600),
    safety_failure character varying(550) NOT NULL,
    hazard_id character varying(550),
    cm_description text NOT NULL,
    replaced_asset_config_id character varying(500) NOT NULL,
    cm_start_date date NOT NULL,
    cm_start_time time without time zone NOT NULL,
    cm_end_date date,
    cm_end_time time without time zone,
    oem_failure_reference text NOT NULL,
    asset_config_id_id character varying(550) NOT NULL,
    defect_id integer,
    mode_description character varying(600),
    mode_id_id integer,
    asset_type character varying(550) NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 &   DROP TABLE public.fracas_failuredata;
       public         heap    postgres    false            �            1259    57993    fracas_failuredata_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_failuredata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.fracas_failuredata_id_seq;
       public          postgres    false    250            �           0    0    fracas_failuredata_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.fracas_failuredata_id_seq OWNED BY public.fracas_failuredata.id;
          public          postgres    false    251            �            1259    57994    fracas_failuremode    TABLE     5  CREATE TABLE public.fracas_failuremode (
    id integer NOT NULL,
    mode_id character varying(550) NOT NULL,
    asset_type character varying(255)[] NOT NULL,
    end_date date,
    start_date date,
    mode_description character varying(550),
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 &   DROP TABLE public.fracas_failuremode;
       public         heap    postgres    false            �            1259    57999    fracas_failuremode_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_failuremode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.fracas_failuremode_id_seq;
       public          postgres    false    252            �           0    0    fracas_failuremode_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.fracas_failuremode_id_seq OWNED BY public.fracas_failuremode.id;
          public          postgres    false    253            �            1259    58000    fracas_history    TABLE     �   CREATE TABLE public.fracas_history (
    id integer NOT NULL,
    "P_id" integer NOT NULL,
    date date,
    message text NOT NULL,
    "time" time without time zone,
    user_id integer NOT NULL,
    function_name character varying(50)
);
 "   DROP TABLE public.fracas_history;
       public         heap    postgres    false            �            1259    58005    fracas_history_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_history_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.fracas_history_id_seq;
       public          postgres    false    254            �           0    0    fracas_history_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.fracas_history_id_seq OWNED BY public.fracas_history.id;
          public          postgres    false    255                        1259    58006    fracas_pbsmaster    TABLE     �  CREATE TABLE public.fracas_pbsmaster (
    id integer NOT NULL,
    system character varying(550) NOT NULL,
    subsystem character varying(550) NOT NULL,
    product_id character varying(550) NOT NULL,
    product_description character varying(550) NOT NULL,
    asset_type character varying(550) NOT NULL,
    asset_description character varying(550) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MART" double precision NOT NULL,
    asset_quantity integer NOT NULL,
    "MTTR" double precision NOT NULL,
    is_active integer NOT NULL,
    project_id integer,
    availability_target double precision NOT NULL
);
 $   DROP TABLE public.fracas_pbsmaster;
       public         heap    postgres    false                       1259    58011    fracas_pbsmaster_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_pbsmaster_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public.fracas_pbsmaster_id_seq;
       public          postgres    false    256            �           0    0    fracas_pbsmaster_id_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public.fracas_pbsmaster_id_seq OWNED BY public.fracas_pbsmaster.id;
          public          postgres    false    257                       1259    58012    fracas_pbsunit    TABLE     �   CREATE TABLE public.fracas_pbsunit (
    id integer NOT NULL,
    "MTBFMTBSAF" text NOT NULL,
    "MTTR" text NOT NULL,
    average_speed double precision NOT NULL,
    chk_average_speed double precision NOT NULL
);
 "   DROP TABLE public.fracas_pbsunit;
       public         heap    postgres    false                       1259    58017    fracas_pbsunit_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_pbsunit_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.fracas_pbsunit_id_seq;
       public          postgres    false    258            �           0    0    fracas_pbsunit_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.fracas_pbsunit_id_seq OWNED BY public.fracas_pbsunit.id;
          public          postgres    false    259                       1259    58018    fracas_product    TABLE     �  CREATE TABLE public.fracas_product (
    product_id integer NOT NULL,
    product_name character varying(50) NOT NULL,
    description character varying(100) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MTTR" double precision NOT NULL,
    availability_target double precision NOT NULL,
    is_active integer NOT NULL,
    num_of_trains integer NOT NULL
);
 "   DROP TABLE public.fracas_product;
       public         heap    postgres    false                       1259    58021    fracas_product_product_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_product_product_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 4   DROP SEQUENCE public.fracas_product_product_id_seq;
       public          postgres    false    260            �           0    0    fracas_product_product_id_seq    SEQUENCE OWNED BY     _   ALTER SEQUENCE public.fracas_product_product_id_seq OWNED BY public.fracas_product.product_id;
          public          postgres    false    261                       1259    58022    fracas_reviewboard    TABLE     l  CREATE TABLE public.fracas_reviewboard (
    id integer NOT NULL,
    asset_type character varying(550) NOT NULL,
    meeting_date date,
    meeting_id character varying(550),
    from_date date,
    to_date date,
    meeting_status character varying(550),
    meeting_outcome character varying(550),
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 &   DROP TABLE public.fracas_reviewboard;
       public         heap    postgres    false                       1259    58027    fracas_reviewboard_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_reviewboard_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 0   DROP SEQUENCE public.fracas_reviewboard_id_seq;
       public          postgres    false    262            �           0    0    fracas_reviewboard_id_seq    SEQUENCE OWNED BY     W   ALTER SEQUENCE public.fracas_reviewboard_id_seq OWNED BY public.fracas_reviewboard.id;
          public          postgres    false    263                       1259    58028    fracas_rootcause    TABLE     �  CREATE TABLE public.fracas_rootcause (
    root_cause_id integer NOT NULL,
    root_cause_description text NOT NULL,
    rca_workshop_date date,
    root_cause_status character varying(550) NOT NULL,
    defect_id integer,
    asset_type character varying(550) NOT NULL,
    immediate_cause character varying(100) NOT NULL,
    leading_reasons character varying(100) NOT NULL,
    "P_id" integer NOT NULL,
    is_active integer NOT NULL
);
 $   DROP TABLE public.fracas_rootcause;
       public         heap    postgres    false            	           1259    58033 "   fracas_rootcause_root_cause_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_rootcause_root_cause_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 9   DROP SEQUENCE public.fracas_rootcause_root_cause_id_seq;
       public          postgres    false    264            �           0    0 "   fracas_rootcause_root_cause_id_seq    SEQUENCE OWNED BY     i   ALTER SEQUENCE public.fracas_rootcause_root_cause_id_seq OWNED BY public.fracas_rootcause.root_cause_id;
          public          postgres    false    265                       1259    58380    fracas_systems    TABLE     M  CREATE TABLE public.fracas_systems (
    id integer NOT NULL,
    "System" character varying(550) NOT NULL,
    "MTBF" double precision NOT NULL,
    "MTBSAF" double precision NOT NULL,
    "MTTR" double precision NOT NULL,
    availability_target double precision NOT NULL,
    is_active integer NOT NULL,
    project_id integer
);
 "   DROP TABLE public.fracas_systems;
       public         heap    postgres    false                       1259    58379    fracas_systems_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_systems_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public.fracas_systems_id_seq;
       public          postgres    false    281            �           0    0    fracas_systems_id_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public.fracas_systems_id_seq OWNED BY public.fracas_systems.id;
          public          postgres    false    280            
           1259    58034     fracas_temp_table_asset_register    TABLE     q  CREATE TABLE public.fracas_temp_table_asset_register (
    id integer NOT NULL,
    asset_config_id character varying(550) NOT NULL,
    asset_serial_number character varying(550) NOT NULL,
    location_id text NOT NULL,
    location_description text NOT NULL,
    asset_type text NOT NULL,
    asset_type_id text NOT NULL,
    software_version character varying(550) NOT NULL,
    asset_description text NOT NULL,
    software_description text NOT NULL,
    asset_status character varying(550) NOT NULL,
    is_active integer NOT NULL,
    "P_id" text NOT NULL,
    error_list text NOT NULL,
    updated_by text NOT NULL
);
 4   DROP TABLE public.fracas_temp_table_asset_register;
       public         heap    postgres    false                       1259    58039 '   fracas_temp_table_asset_register_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_temp_table_asset_register_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 >   DROP SEQUENCE public.fracas_temp_table_asset_register_id_seq;
       public          postgres    false    266            �           0    0 '   fracas_temp_table_asset_register_id_seq    SEQUENCE OWNED BY     s   ALTER SEQUENCE public.fracas_temp_table_asset_register_id_seq OWNED BY public.fracas_temp_table_asset_register.id;
          public          postgres    false    267                       1259    58040    fracas_temp_table_failure_data    TABLE     j  CREATE TABLE public.fracas_temp_table_failure_data (
    id integer NOT NULL,
    failure_id bigint,
    asset_type text NOT NULL,
    asset_config_id text NOT NULL,
    asset_type_id text NOT NULL,
    event_description text NOT NULL,
    mode_id text NOT NULL,
    date text NOT NULL,
    "time" text NOT NULL,
    detection text NOT NULL,
    service_delay text NOT NULL,
    immediate_investigation text NOT NULL,
    failure_type text NOT NULL,
    safety_failure text NOT NULL,
    hazard_id text NOT NULL,
    cm_description text NOT NULL,
    replaced_asset_config_id text NOT NULL,
    cm_start_date text NOT NULL,
    cm_start_time text NOT NULL,
    cm_end_date text NOT NULL,
    cm_end_time text NOT NULL,
    oem_failure_reference text NOT NULL,
    defect text NOT NULL,
    error_list text NOT NULL,
    "P_id" text NOT NULL,
    updated_by text NOT NULL
);
 2   DROP TABLE public.fracas_temp_table_failure_data;
       public         heap    postgres    false                       1259    58045 %   fracas_temp_table_failure_data_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_temp_table_failure_data_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public.fracas_temp_table_failure_data_id_seq;
       public          postgres    false    268            �           0    0 %   fracas_temp_table_failure_data_id_seq    SEQUENCE OWNED BY     o   ALTER SEQUENCE public.fracas_temp_table_failure_data_id_seq OWNED BY public.fracas_temp_table_failure_data.id;
          public          postgres    false    269                       1259    58046    fracas_temp_table_failure_mode    TABLE     $  CREATE TABLE public.fracas_temp_table_failure_mode (
    id integer NOT NULL,
    mode_id text NOT NULL,
    mode_description text NOT NULL,
    asset_type text NOT NULL,
    asset_type_id text NOT NULL,
    "P_id" text NOT NULL,
    updated_by text NOT NULL,
    error_list text NOT NULL
);
 2   DROP TABLE public.fracas_temp_table_failure_mode;
       public         heap    postgres    false                       1259    58051 %   fracas_temp_table_failure_mode_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_temp_table_failure_mode_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 <   DROP SEQUENCE public.fracas_temp_table_failure_mode_id_seq;
       public          postgres    false    270            �           0    0 %   fracas_temp_table_failure_mode_id_seq    SEQUENCE OWNED BY     o   ALTER SEQUENCE public.fracas_temp_table_failure_mode_id_seq OWNED BY public.fracas_temp_table_failure_mode.id;
          public          postgres    false    271                       1259    58052    fracas_temp_table_failuredata    TABLE     r  CREATE TABLE public.fracas_temp_table_failuredata (
    id integer NOT NULL,
    asset_type text NOT NULL,
    failure_id text NOT NULL,
    asset_config_id text NOT NULL,
    event_description text NOT NULL,
    mode_id text NOT NULL,
    mode_description text NOT NULL,
    date text NOT NULL,
    "time" text NOT NULL,
    detection text NOT NULL,
    service_delay text NOT NULL,
    immediate_investigation text NOT NULL,
    failure_type text NOT NULL,
    safety_failure text NOT NULL,
    hazard_id text NOT NULL,
    cm_description text NOT NULL,
    replaced_asset_config_id text NOT NULL,
    cm_start_date text NOT NULL,
    cm_start_time text NOT NULL,
    cm_end_date text NOT NULL,
    cm_end_time text NOT NULL,
    oem_failure_reference text NOT NULL,
    defect text NOT NULL,
    "P_id" text NOT NULL,
    is_active text NOT NULL,
    updated_by text NOT NULL
);
 1   DROP TABLE public.fracas_temp_table_failuredata;
       public         heap    postgres    false                       1259    58057 $   fracas_temp_table_failuredata_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_temp_table_failuredata_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.fracas_temp_table_failuredata_id_seq;
       public          postgres    false    272            �           0    0 $   fracas_temp_table_failuredata_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.fracas_temp_table_failuredata_id_seq OWNED BY public.fracas_temp_table_failuredata.id;
          public          postgres    false    273                       1259    58058    fracas_temp_table_import_file    TABLE       CREATE TABLE public.fracas_temp_table_import_file (
    id integer NOT NULL,
    system text NOT NULL,
    subsystem text NOT NULL,
    subsystem_id integer NOT NULL,
    product_id character varying(550) NOT NULL,
    product_description text NOT NULL,
    asset_type text NOT NULL,
    asset_description text NOT NULL,
    "MTBF" text NOT NULL,
    "MTBSAF" text NOT NULL,
    "MTTR" text NOT NULL,
    "MART" text NOT NULL,
    asset_quantity text NOT NULL,
    error_list text NOT NULL,
    updated_by text NOT NULL
);
 1   DROP TABLE public.fracas_temp_table_import_file;
       public         heap    postgres    false                       1259    58063 $   fracas_temp_table_import_file_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_temp_table_import_file_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ;   DROP SEQUENCE public.fracas_temp_table_import_file_id_seq;
       public          postgres    false    274            �           0    0 $   fracas_temp_table_import_file_id_seq    SEQUENCE OWNED BY     m   ALTER SEQUENCE public.fracas_temp_table_import_file_id_seq OWNED BY public.fracas_temp_table_import_file.id;
          public          postgres    false    275                       1259    58064    fracas_userprofile_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_userprofile_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;
 0   DROP SEQUENCE public.fracas_userprofile_id_seq;
       public          postgres    false                       1259    58065    fracas_userprofile    TABLE     �  CREATE TABLE public.fracas_userprofile (
    id integer DEFAULT nextval('public.fracas_userprofile_id_seq'::regclass) NOT NULL,
    first_name character varying(50) NOT NULL,
    last_name character varying(50) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    user_id integer NOT NULL,
    product_id_id integer,
    user_role_id integer,
    is_active integer NOT NULL,
    is_disable integer NOT NULL
);
 &   DROP TABLE public.fracas_userprofile;
       public         heap    postgres    false    276                       1259    58069    fracas_userresetkey_id_seq    SEQUENCE     �   CREATE SEQUENCE public.fracas_userresetkey_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    MAXVALUE 2147483647
    CACHE 1;
 1   DROP SEQUENCE public.fracas_userresetkey_id_seq;
       public          postgres    false                       1259    58070    fracas_userresetkey    TABLE     M  CREATE TABLE public.fracas_userresetkey (
    id integer DEFAULT nextval('public.fracas_userresetkey_id_seq'::regclass) NOT NULL,
    key character varying(255) NOT NULL,
    expires_on timestamp with time zone,
    otp_expires_on timestamp with time zone,
    date timestamp with time zone NOT NULL,
    user_id integer NOT NULL
);
 '   DROP TABLE public.fracas_userresetkey;
       public         heap    postgres    false    278                       2604    58074 '   admin_tools_stats_criteriatostatsm2m id    DEFAULT     �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m ALTER COLUMN id SET DEFAULT nextval('public.admin_tools_stats_criteriatostatsm2m_id_seq'::regclass);
 V   ALTER TABLE public.admin_tools_stats_criteriatostatsm2m ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    210    209                       2604    58075    auth_group id    DEFAULT     n   ALTER TABLE ONLY public.auth_group ALTER COLUMN id SET DEFAULT nextval('public.auth_group_id_seq'::regclass);
 <   ALTER TABLE public.auth_group ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    212    211                       2604    58076    auth_group_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_group_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_group_permissions_id_seq'::regclass);
 H   ALTER TABLE public.auth_group_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    214    213                       2604    58077    auth_permission id    DEFAULT     x   ALTER TABLE ONLY public.auth_permission ALTER COLUMN id SET DEFAULT nextval('public.auth_permission_id_seq'::regclass);
 A   ALTER TABLE public.auth_permission ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    216    215                       2604    58078    auth_user id    DEFAULT     l   ALTER TABLE ONLY public.auth_user ALTER COLUMN id SET DEFAULT nextval('public.auth_user_id_seq'::regclass);
 ;   ALTER TABLE public.auth_user ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    220    217                       2604    58079    auth_user_groups id    DEFAULT     z   ALTER TABLE ONLY public.auth_user_groups ALTER COLUMN id SET DEFAULT nextval('public.auth_user_groups_id_seq'::regclass);
 B   ALTER TABLE public.auth_user_groups ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    219    218                       2604    58080    auth_user_user_permissions id    DEFAULT     �   ALTER TABLE ONLY public.auth_user_user_permissions ALTER COLUMN id SET DEFAULT nextval('public.auth_user_user_permissions_id_seq'::regclass);
 L   ALTER TABLE public.auth_user_user_permissions ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    222    221                       2604    58081    dash_stats_criteria id    DEFAULT     �   ALTER TABLE ONLY public.dash_stats_criteria ALTER COLUMN id SET DEFAULT nextval('public.dash_stats_criteria_id_seq'::regclass);
 E   ALTER TABLE public.dash_stats_criteria ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    224    223                       2604    58082    dashboard_stats id    DEFAULT     x   ALTER TABLE ONLY public.dashboard_stats ALTER COLUMN id SET DEFAULT nextval('public.dashboard_stats_id_seq'::regclass);
 A   ALTER TABLE public.dashboard_stats ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    226    225                       2604    58083    django_admin_log id    DEFAULT     z   ALTER TABLE ONLY public.django_admin_log ALTER COLUMN id SET DEFAULT nextval('public.django_admin_log_id_seq'::regclass);
 B   ALTER TABLE public.django_admin_log ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    228    227                       2604    58084    django_content_type id    DEFAULT     �   ALTER TABLE ONLY public.django_content_type ALTER COLUMN id SET DEFAULT nextval('public.django_content_type_id_seq'::regclass);
 E   ALTER TABLE public.django_content_type ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    230    229                       2604    58085    django_migrations id    DEFAULT     |   ALTER TABLE ONLY public.django_migrations ALTER COLUMN id SET DEFAULT nextval('public.django_migrations_id_seq'::regclass);
 C   ALTER TABLE public.django_migrations ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    232    231                       2604    58086    fracas_action action_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_action ALTER COLUMN action_id SET DEFAULT nextval('public.fracas_action_action_id_seq'::regclass);
 F   ALTER TABLE public.fracas_action ALTER COLUMN action_id DROP DEFAULT;
       public          postgres    false    235    234                        2604    58087    fracas_asset id    DEFAULT     r   ALTER TABLE ONLY public.fracas_asset ALTER COLUMN id SET DEFAULT nextval('public.fracas_asset_id_seq'::regclass);
 >   ALTER TABLE public.fracas_asset ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    237    236            !           2604    58088    fracas_assetregister id    DEFAULT     �   ALTER TABLE ONLY public.fracas_assetregister ALTER COLUMN id SET DEFAULT nextval('public.fracas_assetregister_id_seq'::regclass);
 F   ALTER TABLE public.fracas_assetregister ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    239    238            "           2604    58089 ,   fracas_correctiveaction corrective_action_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_correctiveaction ALTER COLUMN corrective_action_id SET DEFAULT nextval('public.fracas_correctiveaction_corrective_action_id_seq'::regclass);
 [   ALTER TABLE public.fracas_correctiveaction ALTER COLUMN corrective_action_id DROP DEFAULT;
       public          postgres    false    241    240            #           2604    58090    fracas_defect defect_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_defect ALTER COLUMN defect_id SET DEFAULT nextval('public.fracas_defect_defect_id_seq'::regclass);
 F   ALTER TABLE public.fracas_defect ALTER COLUMN defect_id DROP DEFAULT;
       public          postgres    false    243    242            $           2604    58091 ,   fracas_defectdiscussion defect_discussion_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_defectdiscussion ALTER COLUMN defect_discussion_id SET DEFAULT nextval('public.fracas_defectdiscussion_defect_discussion_id_seq'::regclass);
 [   ALTER TABLE public.fracas_defectdiscussion ALTER COLUMN defect_discussion_id DROP DEFAULT;
       public          postgres    false    247    244            %           2604    58092 $   fracas_defectdiscussion_attendees id    DEFAULT     �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees ALTER COLUMN id SET DEFAULT nextval('public.fracas_defectdiscussion_attendees_id_seq'::regclass);
 S   ALTER TABLE public.fracas_defectdiscussion_attendees ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    246    245            &           2604    58093    fracas_employeemaster id    DEFAULT     �   ALTER TABLE ONLY public.fracas_employeemaster ALTER COLUMN id SET DEFAULT nextval('public.fracas_employeemaster_id_seq'::regclass);
 G   ALTER TABLE public.fracas_employeemaster ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    249    248            '           2604    58094    fracas_failuredata id    DEFAULT     ~   ALTER TABLE ONLY public.fracas_failuredata ALTER COLUMN id SET DEFAULT nextval('public.fracas_failuredata_id_seq'::regclass);
 D   ALTER TABLE public.fracas_failuredata ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    251    250            (           2604    58095    fracas_failuremode id    DEFAULT     ~   ALTER TABLE ONLY public.fracas_failuremode ALTER COLUMN id SET DEFAULT nextval('public.fracas_failuremode_id_seq'::regclass);
 D   ALTER TABLE public.fracas_failuremode ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    253    252            )           2604    58096    fracas_history id    DEFAULT     v   ALTER TABLE ONLY public.fracas_history ALTER COLUMN id SET DEFAULT nextval('public.fracas_history_id_seq'::regclass);
 @   ALTER TABLE public.fracas_history ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    255    254            *           2604    58097    fracas_pbsmaster id    DEFAULT     z   ALTER TABLE ONLY public.fracas_pbsmaster ALTER COLUMN id SET DEFAULT nextval('public.fracas_pbsmaster_id_seq'::regclass);
 B   ALTER TABLE public.fracas_pbsmaster ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    257    256            +           2604    58098    fracas_pbsunit id    DEFAULT     v   ALTER TABLE ONLY public.fracas_pbsunit ALTER COLUMN id SET DEFAULT nextval('public.fracas_pbsunit_id_seq'::regclass);
 @   ALTER TABLE public.fracas_pbsunit ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    259    258            ,           2604    58099    fracas_product product_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_product ALTER COLUMN product_id SET DEFAULT nextval('public.fracas_product_product_id_seq'::regclass);
 H   ALTER TABLE public.fracas_product ALTER COLUMN product_id DROP DEFAULT;
       public          postgres    false    261    260            -           2604    58100    fracas_reviewboard id    DEFAULT     ~   ALTER TABLE ONLY public.fracas_reviewboard ALTER COLUMN id SET DEFAULT nextval('public.fracas_reviewboard_id_seq'::regclass);
 D   ALTER TABLE public.fracas_reviewboard ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    263    262            .           2604    58101    fracas_rootcause root_cause_id    DEFAULT     �   ALTER TABLE ONLY public.fracas_rootcause ALTER COLUMN root_cause_id SET DEFAULT nextval('public.fracas_rootcause_root_cause_id_seq'::regclass);
 M   ALTER TABLE public.fracas_rootcause ALTER COLUMN root_cause_id DROP DEFAULT;
       public          postgres    false    265    264            6           2604    58383    fracas_systems id    DEFAULT     v   ALTER TABLE ONLY public.fracas_systems ALTER COLUMN id SET DEFAULT nextval('public.fracas_systems_id_seq'::regclass);
 @   ALTER TABLE public.fracas_systems ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    280    281    281            /           2604    58102 #   fracas_temp_table_asset_register id    DEFAULT     �   ALTER TABLE ONLY public.fracas_temp_table_asset_register ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_asset_register_id_seq'::regclass);
 R   ALTER TABLE public.fracas_temp_table_asset_register ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    267    266            0           2604    58103 !   fracas_temp_table_failure_data id    DEFAULT     �   ALTER TABLE ONLY public.fracas_temp_table_failure_data ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failure_data_id_seq'::regclass);
 P   ALTER TABLE public.fracas_temp_table_failure_data ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    269    268            1           2604    58104 !   fracas_temp_table_failure_mode id    DEFAULT     �   ALTER TABLE ONLY public.fracas_temp_table_failure_mode ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failure_mode_id_seq'::regclass);
 P   ALTER TABLE public.fracas_temp_table_failure_mode ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    271    270            2           2604    58105     fracas_temp_table_failuredata id    DEFAULT     �   ALTER TABLE ONLY public.fracas_temp_table_failuredata ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_failuredata_id_seq'::regclass);
 O   ALTER TABLE public.fracas_temp_table_failuredata ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    273    272            3           2604    58106     fracas_temp_table_import_file id    DEFAULT     �   ALTER TABLE ONLY public.fracas_temp_table_import_file ALTER COLUMN id SET DEFAULT nextval('public.fracas_temp_table_import_file_id_seq'::regclass);
 O   ALTER TABLE public.fracas_temp_table_import_file ALTER COLUMN id DROP DEFAULT;
       public          postgres    false    275    274            j          0    57877 $   admin_tools_stats_criteriatostatsm2m 
   TABLE DATA           r   COPY public.admin_tools_stats_criteriatostatsm2m (id, "order", prefix, use_as, criteria_id, stats_id) FROM stdin;
    public          postgres    false    209    �      l          0    57882 
   auth_group 
   TABLE DATA           .   COPY public.auth_group (id, name) FROM stdin;
    public          postgres    false    211   =�      n          0    57886    auth_group_permissions 
   TABLE DATA           M   COPY public.auth_group_permissions (id, group_id, permission_id) FROM stdin;
    public          postgres    false    213   ��      p          0    57890    auth_permission 
   TABLE DATA           N   COPY public.auth_permission (id, name, content_type_id, codename) FROM stdin;
    public          postgres    false    215   ��      r          0    57894 	   auth_user 
   TABLE DATA           �   COPY public.auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined, role) FROM stdin;
    public          postgres    false    217   �      s          0    57900    auth_user_groups 
   TABLE DATA           A   COPY public.auth_user_groups (id, user_id, group_id) FROM stdin;
    public          postgres    false    218   �      v          0    57905    auth_user_user_permissions 
   TABLE DATA           P   COPY public.auth_user_user_permissions (id, user_id, permission_id) FROM stdin;
    public          postgres    false    221   �      x          0    57909    dash_stats_criteria 
   TABLE DATA           �   COPY public.dash_stats_criteria (id, criteria_name, criteria_fix_mapping, dynamic_criteria_field_name, criteria_dynamic_mapping, created_date, updated_date) FROM stdin;
    public          postgres    false    223   ;�      z          0    57915    dashboard_stats 
   TABLE DATA           4  COPY public.dashboard_stats (id, graph_key, graph_title, model_app_name, model_name, date_field_name, operation_field_name, type_operation_field_name, is_visible, created_date, updated_date, user_field_name, default_chart_type, default_time_period, default_time_scale, y_axis_format, "distinct") FROM stdin;
    public          postgres    false    225   X�      |          0    57922    django_admin_log 
   TABLE DATA           �   COPY public.django_admin_log (id, action_time, object_id, object_repr, action_flag, change_message, content_type_id, user_id) FROM stdin;
    public          postgres    false    227   u�      ~          0    57929    django_content_type 
   TABLE DATA           C   COPY public.django_content_type (id, app_label, model) FROM stdin;
    public          postgres    false    229   ��      �          0    57933    django_migrations 
   TABLE DATA           C   COPY public.django_migrations (id, app, name, applied) FROM stdin;
    public          postgres    false    231   ��      �          0    57939    django_session 
   TABLE DATA           P   COPY public.django_session (session_key, session_data, expire_date) FROM stdin;
    public          postgres    false    233   9      �          0    57944    fracas_action 
   TABLE DATA           �   COPY public.fracas_action (action_id, action_description, action_owner, action_status, action_due_date, progress_log, defect_discussion_id_id) FROM stdin;
    public          postgres    false    234   9,      �          0    57950    fracas_asset 
   TABLE DATA           �   COPY public.fracas_asset (id, asset_config_id, location_id, location_description, asset_serial_number, asset_type, asset_description, software_version, software_description, asset_status, is_active, "P_id") FROM stdin;
    public          postgres    false    236   �,      �          0    57956    fracas_assetregister 
   TABLE DATA           2   COPY public.fracas_assetregister (id) FROM stdin;
    public          postgres    false    238   Xj      �          0    57960    fracas_correctiveaction 
   TABLE DATA           �   COPY public.fracas_correctiveaction (corrective_action_id, corrective_action_owner, corrective_action_description, corrective_action_update, corrective_action_status, defect_id, "P_id", is_active) FROM stdin;
    public          postgres    false    240   uj      �          0    57966    fracas_defect 
   TABLE DATA           �   COPY public.fracas_defect (start_date, end_date, asset_type, defect_id, defect_description, defect_open_date, defect_closed_date, investigation, defect_status, defect_status_remarks, oem_defect_reference, oem_target_date, "P_id", is_active) FROM stdin;
    public          postgres    false    242   �k      �          0    57972    fracas_defectdiscussion 
   TABLE DATA           ~   COPY public.fracas_defectdiscussion (defect_discussion_id, meeting_date, defect_id, review_board_id, description) FROM stdin;
    public          postgres    false    244   n      �          0    57977 !   fracas_defectdiscussion_attendees 
   TABLE DATA           d   COPY public.fracas_defectdiscussion_attendees (id, defectdiscussion_id, userprofile_id) FROM stdin;
    public          postgres    false    245   �n      �          0    57982    fracas_employeemaster 
   TABLE DATA           S   COPY public.fracas_employeemaster (id, employee_id, name, designation) FROM stdin;
    public          postgres    false    248   �n      �          0    57988    fracas_failuredata 
   TABLE DATA           �  COPY public.fracas_failuredata (id, failure_id, event_description, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, asset_config_id_id, defect_id, mode_description, mode_id_id, asset_type, "P_id", is_active) FROM stdin;
    public          postgres    false    250   �n      �          0    57994    fracas_failuremode 
   TABLE DATA           �   COPY public.fracas_failuremode (id, mode_id, asset_type, end_date, start_date, mode_description, "P_id", is_active) FROM stdin;
    public          postgres    false    252   xq      �          0    58000    fracas_history 
   TABLE DATA           c   COPY public.fracas_history (id, "P_id", date, message, "time", user_id, function_name) FROM stdin;
    public          postgres    false    254   os      �          0    58006    fracas_pbsmaster 
   TABLE DATA           �   COPY public.fracas_pbsmaster (id, system, subsystem, product_id, product_description, asset_type, asset_description, "MTBF", "MTBSAF", "MART", asset_quantity, "MTTR", is_active, project_id, availability_target) FROM stdin;
    public          postgres    false    256   n~      �          0    58012    fracas_pbsunit 
   TABLE DATA           d   COPY public.fracas_pbsunit (id, "MTBFMTBSAF", "MTTR", average_speed, chk_average_speed) FROM stdin;
    public          postgres    false    258   ]�      �          0    58018    fracas_product 
   TABLE DATA           �   COPY public.fracas_product (product_id, product_name, description, "MTBF", "MTBSAF", "MTTR", availability_target, is_active, num_of_trains) FROM stdin;
    public          postgres    false    260   ��      �          0    58022    fracas_reviewboard 
   TABLE DATA           �   COPY public.fracas_reviewboard (id, asset_type, meeting_date, meeting_id, from_date, to_date, meeting_status, meeting_outcome, "P_id", is_active) FROM stdin;
    public          postgres    false    262   J�      �          0    58028    fracas_rootcause 
   TABLE DATA           �   COPY public.fracas_rootcause (root_cause_id, root_cause_description, rca_workshop_date, root_cause_status, defect_id, asset_type, immediate_cause, leading_reasons, "P_id", is_active) FROM stdin;
    public          postgres    false    264   Ր      �          0    58380    fracas_systems 
   TABLE DATA           |   COPY public.fracas_systems (id, "System", "MTBF", "MTBSAF", "MTTR", availability_target, is_active, project_id) FROM stdin;
    public          postgres    false    281   ��      �          0    58034     fracas_temp_table_asset_register 
   TABLE DATA             COPY public.fracas_temp_table_asset_register (id, asset_config_id, asset_serial_number, location_id, location_description, asset_type, asset_type_id, software_version, asset_description, software_description, asset_status, is_active, "P_id", error_list, updated_by) FROM stdin;
    public          postgres    false    266   a�      �          0    58040    fracas_temp_table_failure_data 
   TABLE DATA           �  COPY public.fracas_temp_table_failure_data (id, failure_id, asset_type, asset_config_id, asset_type_id, event_description, mode_id, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, defect, error_list, "P_id", updated_by) FROM stdin;
    public          postgres    false    268   ~�      �          0    58046    fracas_temp_table_failure_mode 
   TABLE DATA           �   COPY public.fracas_temp_table_failure_mode (id, mode_id, mode_description, asset_type, asset_type_id, "P_id", updated_by, error_list) FROM stdin;
    public          postgres    false    270   ��      �          0    58052    fracas_temp_table_failuredata 
   TABLE DATA           �  COPY public.fracas_temp_table_failuredata (id, asset_type, failure_id, asset_config_id, event_description, mode_id, mode_description, date, "time", detection, service_delay, immediate_investigation, failure_type, safety_failure, hazard_id, cm_description, replaced_asset_config_id, cm_start_date, cm_start_time, cm_end_date, cm_end_time, oem_failure_reference, defect, "P_id", is_active, updated_by) FROM stdin;
    public          postgres    false    272   ��      �          0    58058    fracas_temp_table_import_file 
   TABLE DATA           �   COPY public.fracas_temp_table_import_file (id, system, subsystem, subsystem_id, product_id, product_description, asset_type, asset_description, "MTBF", "MTBSAF", "MTTR", "MART", asset_quantity, error_list, updated_by) FROM stdin;
    public          postgres    false    274   Ւ      �          0    58065    fracas_userprofile 
   TABLE DATA           �   COPY public.fracas_userprofile (id, first_name, last_name, created_at, updated_at, user_id, product_id_id, user_role_id, is_active, is_disable) FROM stdin;
    public          postgres    false    277   �      �          0    58070    fracas_userresetkey 
   TABLE DATA           a   COPY public.fracas_userresetkey (id, key, expires_on, otp_expires_on, date, user_id) FROM stdin;
    public          postgres    false    279   h�      �           0    0 +   admin_tools_stats_criteriatostatsm2m_id_seq    SEQUENCE SET     Z   SELECT pg_catalog.setval('public.admin_tools_stats_criteriatostatsm2m_id_seq', 1, false);
          public          postgres    false    210            �           0    0    auth_group_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_group_id_seq', 1, true);
          public          postgres    false    212            �           0    0    auth_group_permissions_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.auth_group_permissions_id_seq', 1, false);
          public          postgres    false    214            �           0    0    auth_permission_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_permission_id_seq', 132, true);
          public          postgres    false    216            �           0    0    auth_user_groups_id_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public.auth_user_groups_id_seq', 1, false);
          public          postgres    false    219            �           0    0    auth_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.auth_user_id_seq', 38, true);
          public          postgres    false    220            �           0    0 !   auth_user_user_permissions_id_seq    SEQUENCE SET     P   SELECT pg_catalog.setval('public.auth_user_user_permissions_id_seq', 1, false);
          public          postgres    false    222            �           0    0    dash_stats_criteria_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.dash_stats_criteria_id_seq', 1, false);
          public          postgres    false    224            �           0    0    dashboard_stats_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.dashboard_stats_id_seq', 1, false);
          public          postgres    false    226            �           0    0    django_admin_log_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_admin_log_id_seq', 4254, true);
          public          postgres    false    228            �           0    0    django_content_type_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.django_content_type_id_seq', 33, true);
          public          postgres    false    230            �           0    0    django_migrations_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.django_migrations_id_seq', 152, true);
          public          postgres    false    232            �           0    0    fracas_action_action_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.fracas_action_action_id_seq', 35, true);
          public          postgres    false    235            �           0    0    fracas_asset_id_seq    SEQUENCE SET     D   SELECT pg_catalog.setval('public.fracas_asset_id_seq', 1770, true);
          public          postgres    false    237            �           0    0    fracas_assetregister_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.fracas_assetregister_id_seq', 1, false);
          public          postgres    false    239            �           0    0 0   fracas_correctiveaction_corrective_action_id_seq    SEQUENCE SET     `   SELECT pg_catalog.setval('public.fracas_correctiveaction_corrective_action_id_seq', 127, true);
          public          postgres    false    241            �           0    0    fracas_defect_defect_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.fracas_defect_defect_id_seq', 188, true);
          public          postgres    false    243            �           0    0 (   fracas_defectdiscussion_attendees_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public.fracas_defectdiscussion_attendees_id_seq', 55, true);
          public          postgres    false    246            �           0    0 0   fracas_defectdiscussion_defect_discussion_id_seq    SEQUENCE SET     _   SELECT pg_catalog.setval('public.fracas_defectdiscussion_defect_discussion_id_seq', 77, true);
          public          postgres    false    247            �           0    0    fracas_employeemaster_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.fracas_employeemaster_id_seq', 16, true);
          public          postgres    false    249            �           0    0    fracas_failuredata_id_seq    SEQUENCE SET     K   SELECT pg_catalog.setval('public.fracas_failuredata_id_seq', 28744, true);
          public          postgres    false    251            �           0    0    fracas_failuremode_id_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public.fracas_failuremode_id_seq', 2070, true);
          public          postgres    false    253            �           0    0    fracas_history_id_seq    SEQUENCE SET     E   SELECT pg_catalog.setval('public.fracas_history_id_seq', 961, true);
          public          postgres    false    255            �           0    0    fracas_pbsmaster_id_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public.fracas_pbsmaster_id_seq', 434, true);
          public          postgres    false    257            �           0    0    fracas_pbsunit_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.fracas_pbsunit_id_seq', 3, true);
          public          postgres    false    259            �           0    0    fracas_product_product_id_seq    SEQUENCE SET     L   SELECT pg_catalog.setval('public.fracas_product_product_id_seq', 10, true);
          public          postgres    false    261            �           0    0    fracas_reviewboard_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.fracas_reviewboard_id_seq', 81, true);
          public          postgres    false    263            �           0    0 "   fracas_rootcause_root_cause_id_seq    SEQUENCE SET     Q   SELECT pg_catalog.setval('public.fracas_rootcause_root_cause_id_seq', 86, true);
          public          postgres    false    265            �           0    0    fracas_systems_id_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public.fracas_systems_id_seq', 2, true);
          public          postgres    false    280            �           0    0 '   fracas_temp_table_asset_register_id_seq    SEQUENCE SET     W   SELECT pg_catalog.setval('public.fracas_temp_table_asset_register_id_seq', 198, true);
          public          postgres    false    267            �           0    0 %   fracas_temp_table_failure_data_id_seq    SEQUENCE SET     V   SELECT pg_catalog.setval('public.fracas_temp_table_failure_data_id_seq', 1675, true);
          public          postgres    false    269            �           0    0 %   fracas_temp_table_failure_mode_id_seq    SEQUENCE SET     T   SELECT pg_catalog.setval('public.fracas_temp_table_failure_mode_id_seq', 14, true);
          public          postgres    false    271            �           0    0 $   fracas_temp_table_failuredata_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.fracas_temp_table_failuredata_id_seq', 1, false);
          public          postgres    false    273            �           0    0 $   fracas_temp_table_import_file_id_seq    SEQUENCE SET     S   SELECT pg_catalog.setval('public.fracas_temp_table_import_file_id_seq', 23, true);
          public          postgres    false    275            �           0    0    fracas_userprofile_id_seq    SEQUENCE SET     H   SELECT pg_catalog.setval('public.fracas_userprofile_id_seq', 24, true);
          public          postgres    false    276            �           0    0    fracas_userresetkey_id_seq    SEQUENCE SET     I   SELECT pg_catalog.setval('public.fracas_userresetkey_id_seq', 1, false);
          public          postgres    false    278            9           2606    58108 S   admin_tools_stats_criteriatostatsm2m admin_tools_stats_criteriatostatsm2m_order_key 
   CONSTRAINT     �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_criteriatostatsm2m_order_key UNIQUE ("order");
 }   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m DROP CONSTRAINT admin_tools_stats_criteriatostatsm2m_order_key;
       public            postgres    false    209            ;           2606    58110 N   admin_tools_stats_criteriatostatsm2m admin_tools_stats_criteriatostatsm2m_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_criteriatostatsm2m_pkey PRIMARY KEY (id);
 x   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m DROP CONSTRAINT admin_tools_stats_criteriatostatsm2m_pkey;
       public            postgres    false    209            ?           2606    58112    auth_group auth_group_name_key 
   CONSTRAINT     Y   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_name_key UNIQUE (name);
 H   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_name_key;
       public            postgres    false    211            D           2606    58114 R   auth_group_permissions auth_group_permissions_group_id_permission_id_0cd325b0_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq UNIQUE (group_id, permission_id);
 |   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_permission_id_0cd325b0_uniq;
       public            postgres    false    213    213            G           2606    58116 2   auth_group_permissions auth_group_permissions_pkey 
   CONSTRAINT     p   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_pkey PRIMARY KEY (id);
 \   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_pkey;
       public            postgres    false    213            A           2606    58118    auth_group auth_group_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.auth_group
    ADD CONSTRAINT auth_group_pkey PRIMARY KEY (id);
 D   ALTER TABLE ONLY public.auth_group DROP CONSTRAINT auth_group_pkey;
       public            postgres    false    211            J           2606    58120 F   auth_permission auth_permission_content_type_id_codename_01ab375a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq UNIQUE (content_type_id, codename);
 p   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_codename_01ab375a_uniq;
       public            postgres    false    215    215            L           2606    58122 $   auth_permission auth_permission_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_pkey;
       public            postgres    false    215            T           2606    58124 &   auth_user_groups auth_user_groups_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_pkey;
       public            postgres    false    218            W           2606    58126 @   auth_user_groups auth_user_groups_user_id_group_id_94350c0c_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq UNIQUE (user_id, group_id);
 j   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_group_id_94350c0c_uniq;
       public            postgres    false    218    218            N           2606    58128    auth_user auth_user_pkey 
   CONSTRAINT     V   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_pkey PRIMARY KEY (id);
 B   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_pkey;
       public            postgres    false    217            Z           2606    58130 :   auth_user_user_permissions auth_user_user_permissions_pkey 
   CONSTRAINT     x   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_pkey PRIMARY KEY (id);
 d   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_pkey;
       public            postgres    false    221            ]           2606    58132 Y   auth_user_user_permissions auth_user_user_permissions_user_id_permission_id_14a6b632_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq UNIQUE (user_id, permission_id);
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_permission_id_14a6b632_uniq;
       public            postgres    false    221    221            Q           2606    58134     auth_user auth_user_username_key 
   CONSTRAINT     _   ALTER TABLE ONLY public.auth_user
    ADD CONSTRAINT auth_user_username_key UNIQUE (username);
 J   ALTER TABLE ONLY public.auth_user DROP CONSTRAINT auth_user_username_key;
       public            postgres    false    217            a           2606    58136 ,   dash_stats_criteria dash_stats_criteria_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.dash_stats_criteria
    ADD CONSTRAINT dash_stats_criteria_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.dash_stats_criteria DROP CONSTRAINT dash_stats_criteria_pkey;
       public            postgres    false    223            d           2606    58138 -   dashboard_stats dashboard_stats_graph_key_key 
   CONSTRAINT     m   ALTER TABLE ONLY public.dashboard_stats
    ADD CONSTRAINT dashboard_stats_graph_key_key UNIQUE (graph_key);
 W   ALTER TABLE ONLY public.dashboard_stats DROP CONSTRAINT dashboard_stats_graph_key_key;
       public            postgres    false    225            h           2606    58140 $   dashboard_stats dashboard_stats_pkey 
   CONSTRAINT     b   ALTER TABLE ONLY public.dashboard_stats
    ADD CONSTRAINT dashboard_stats_pkey PRIMARY KEY (id);
 N   ALTER TABLE ONLY public.dashboard_stats DROP CONSTRAINT dashboard_stats_pkey;
       public            postgres    false    225            k           2606    58142 &   django_admin_log django_admin_log_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_pkey;
       public            postgres    false    227            n           2606    58144 E   django_content_type django_content_type_app_label_model_76bd3d3b_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq UNIQUE (app_label, model);
 o   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_app_label_model_76bd3d3b_uniq;
       public            postgres    false    229    229            p           2606    58146 ,   django_content_type django_content_type_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.django_content_type
    ADD CONSTRAINT django_content_type_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.django_content_type DROP CONSTRAINT django_content_type_pkey;
       public            postgres    false    229            r           2606    58148 (   django_migrations django_migrations_pkey 
   CONSTRAINT     f   ALTER TABLE ONLY public.django_migrations
    ADD CONSTRAINT django_migrations_pkey PRIMARY KEY (id);
 R   ALTER TABLE ONLY public.django_migrations DROP CONSTRAINT django_migrations_pkey;
       public            postgres    false    231            u           2606    58150 "   django_session django_session_pkey 
   CONSTRAINT     i   ALTER TABLE ONLY public.django_session
    ADD CONSTRAINT django_session_pkey PRIMARY KEY (session_key);
 L   ALTER TABLE ONLY public.django_session DROP CONSTRAINT django_session_pkey;
       public            postgres    false    233            y           2606    58152     fracas_action fracas_action_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.fracas_action
    ADD CONSTRAINT fracas_action_pkey PRIMARY KEY (action_id);
 J   ALTER TABLE ONLY public.fracas_action DROP CONSTRAINT fracas_action_pkey;
       public            postgres    false    234            |           2606    58154 -   fracas_asset fracas_asset_asset_config_id_key 
   CONSTRAINT     s   ALTER TABLE ONLY public.fracas_asset
    ADD CONSTRAINT fracas_asset_asset_config_id_key UNIQUE (asset_config_id);
 W   ALTER TABLE ONLY public.fracas_asset DROP CONSTRAINT fracas_asset_asset_config_id_key;
       public            postgres    false    236            ~           2606    58156    fracas_asset fracas_asset_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.fracas_asset
    ADD CONSTRAINT fracas_asset_pkey PRIMARY KEY (id);
 H   ALTER TABLE ONLY public.fracas_asset DROP CONSTRAINT fracas_asset_pkey;
       public            postgres    false    236            �           2606    58158 .   fracas_assetregister fracas_assetregister_pkey 
   CONSTRAINT     l   ALTER TABLE ONLY public.fracas_assetregister
    ADD CONSTRAINT fracas_assetregister_pkey PRIMARY KEY (id);
 X   ALTER TABLE ONLY public.fracas_assetregister DROP CONSTRAINT fracas_assetregister_pkey;
       public            postgres    false    238            �           2606    58160 4   fracas_correctiveaction fracas_correctiveaction_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_correctiveaction
    ADD CONSTRAINT fracas_correctiveaction_pkey PRIMARY KEY (corrective_action_id);
 ^   ALTER TABLE ONLY public.fracas_correctiveaction DROP CONSTRAINT fracas_correctiveaction_pkey;
       public            postgres    false    240            �           2606    58162     fracas_defect fracas_defect_pkey 
   CONSTRAINT     e   ALTER TABLE ONLY public.fracas_defect
    ADD CONSTRAINT fracas_defect_pkey PRIMARY KEY (defect_id);
 J   ALTER TABLE ONLY public.fracas_defect DROP CONSTRAINT fracas_defect_pkey;
       public            postgres    false    242            �           2606    58164 a   fracas_defectdiscussion_attendees fracas_defectdiscussion__defectdiscussion_id_empl_4c58967a_uniq 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscussion__defectdiscussion_id_empl_4c58967a_uniq UNIQUE (defectdiscussion_id, userprofile_id);
 �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees DROP CONSTRAINT fracas_defectdiscussion__defectdiscussion_id_empl_4c58967a_uniq;
       public            postgres    false    245    245            �           2606    58166 H   fracas_defectdiscussion_attendees fracas_defectdiscussion_attendees_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscussion_attendees_pkey PRIMARY KEY (id);
 r   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees DROP CONSTRAINT fracas_defectdiscussion_attendees_pkey;
       public            postgres    false    245            �           2606    58168 4   fracas_defectdiscussion fracas_defectdiscussion_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscussion_pkey PRIMARY KEY (defect_discussion_id);
 ^   ALTER TABLE ONLY public.fracas_defectdiscussion DROP CONSTRAINT fracas_defectdiscussion_pkey;
       public            postgres    false    244            �           2606    58170 0   fracas_employeemaster fracas_employeemaster_pkey 
   CONSTRAINT     n   ALTER TABLE ONLY public.fracas_employeemaster
    ADD CONSTRAINT fracas_employeemaster_pkey PRIMARY KEY (id);
 Z   ALTER TABLE ONLY public.fracas_employeemaster DROP CONSTRAINT fracas_employeemaster_pkey;
       public            postgres    false    248            �           2606    58172 *   fracas_failuredata fracas_failuredata_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.fracas_failuredata DROP CONSTRAINT fracas_failuredata_pkey;
       public            postgres    false    250            �           2606    58174 1   fracas_failuremode fracas_failuremode_mode_id_key 
   CONSTRAINT     o   ALTER TABLE ONLY public.fracas_failuremode
    ADD CONSTRAINT fracas_failuremode_mode_id_key UNIQUE (mode_id);
 [   ALTER TABLE ONLY public.fracas_failuremode DROP CONSTRAINT fracas_failuremode_mode_id_key;
       public            postgres    false    252            �           2606    58176 *   fracas_failuremode fracas_failuremode_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.fracas_failuremode
    ADD CONSTRAINT fracas_failuremode_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.fracas_failuremode DROP CONSTRAINT fracas_failuremode_pkey;
       public            postgres    false    252            �           2606    58178 "   fracas_history fracas_history_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.fracas_history
    ADD CONSTRAINT fracas_history_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.fracas_history DROP CONSTRAINT fracas_history_pkey;
       public            postgres    false    254            �           2606    58180 &   fracas_pbsmaster fracas_pbsmaster_pkey 
   CONSTRAINT     d   ALTER TABLE ONLY public.fracas_pbsmaster
    ADD CONSTRAINT fracas_pbsmaster_pkey PRIMARY KEY (id);
 P   ALTER TABLE ONLY public.fracas_pbsmaster DROP CONSTRAINT fracas_pbsmaster_pkey;
       public            postgres    false    256            �           2606    58182 "   fracas_pbsunit fracas_pbsunit_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.fracas_pbsunit
    ADD CONSTRAINT fracas_pbsunit_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.fracas_pbsunit DROP CONSTRAINT fracas_pbsunit_pkey;
       public            postgres    false    258            �           2606    58184 "   fracas_product fracas_product_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.fracas_product
    ADD CONSTRAINT fracas_product_pkey PRIMARY KEY (product_id);
 L   ALTER TABLE ONLY public.fracas_product DROP CONSTRAINT fracas_product_pkey;
       public            postgres    false    260            �           2606    58186 *   fracas_reviewboard fracas_reviewboard_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.fracas_reviewboard
    ADD CONSTRAINT fracas_reviewboard_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.fracas_reviewboard DROP CONSTRAINT fracas_reviewboard_pkey;
       public            postgres    false    262            �           2606    58188 &   fracas_rootcause fracas_rootcause_pkey 
   CONSTRAINT     o   ALTER TABLE ONLY public.fracas_rootcause
    ADD CONSTRAINT fracas_rootcause_pkey PRIMARY KEY (root_cause_id);
 P   ALTER TABLE ONLY public.fracas_rootcause DROP CONSTRAINT fracas_rootcause_pkey;
       public            postgres    false    264            �           2606    58387 "   fracas_systems fracas_systems_pkey 
   CONSTRAINT     `   ALTER TABLE ONLY public.fracas_systems
    ADD CONSTRAINT fracas_systems_pkey PRIMARY KEY (id);
 L   ALTER TABLE ONLY public.fracas_systems DROP CONSTRAINT fracas_systems_pkey;
       public            postgres    false    281            �           2606    58190 F   fracas_temp_table_asset_register fracas_temp_table_asset_register_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_temp_table_asset_register
    ADD CONSTRAINT fracas_temp_table_asset_register_pkey PRIMARY KEY (id);
 p   ALTER TABLE ONLY public.fracas_temp_table_asset_register DROP CONSTRAINT fracas_temp_table_asset_register_pkey;
       public            postgres    false    266            �           2606    58192 B   fracas_temp_table_failure_data fracas_temp_table_failure_data_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_temp_table_failure_data
    ADD CONSTRAINT fracas_temp_table_failure_data_pkey PRIMARY KEY (id);
 l   ALTER TABLE ONLY public.fracas_temp_table_failure_data DROP CONSTRAINT fracas_temp_table_failure_data_pkey;
       public            postgres    false    268            �           2606    58194 B   fracas_temp_table_failure_mode fracas_temp_table_failure_mode_pkey 
   CONSTRAINT     �   ALTER TABLE ONLY public.fracas_temp_table_failure_mode
    ADD CONSTRAINT fracas_temp_table_failure_mode_pkey PRIMARY KEY (id);
 l   ALTER TABLE ONLY public.fracas_temp_table_failure_mode DROP CONSTRAINT fracas_temp_table_failure_mode_pkey;
       public            postgres    false    270            �           2606    58196 @   fracas_temp_table_failuredata fracas_temp_table_failuredata_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.fracas_temp_table_failuredata
    ADD CONSTRAINT fracas_temp_table_failuredata_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.fracas_temp_table_failuredata DROP CONSTRAINT fracas_temp_table_failuredata_pkey;
       public            postgres    false    272            �           2606    58198 @   fracas_temp_table_import_file fracas_temp_table_import_file_pkey 
   CONSTRAINT     ~   ALTER TABLE ONLY public.fracas_temp_table_import_file
    ADD CONSTRAINT fracas_temp_table_import_file_pkey PRIMARY KEY (id);
 j   ALTER TABLE ONLY public.fracas_temp_table_import_file DROP CONSTRAINT fracas_temp_table_import_file_pkey;
       public            postgres    false    274            �           2606    58200 *   fracas_userprofile fracas_userprofile_pkey 
   CONSTRAINT     h   ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_pkey PRIMARY KEY (id);
 T   ALTER TABLE ONLY public.fracas_userprofile DROP CONSTRAINT fracas_userprofile_pkey;
       public            postgres    false    277            �           2606    58202 ,   fracas_userresetkey fracas_userresetkey_pkey 
   CONSTRAINT     j   ALTER TABLE ONLY public.fracas_userresetkey
    ADD CONSTRAINT fracas_userresetkey_pkey PRIMARY KEY (id);
 V   ALTER TABLE ONLY public.fracas_userresetkey DROP CONSTRAINT fracas_userresetkey_pkey;
       public            postgres    false    279            7           1259    58203 9   admin_tools_stats_criteriatostatsm2m_criteria_id_bfe67f05    INDEX     �   CREATE INDEX admin_tools_stats_criteriatostatsm2m_criteria_id_bfe67f05 ON public.admin_tools_stats_criteriatostatsm2m USING btree (criteria_id);
 M   DROP INDEX public.admin_tools_stats_criteriatostatsm2m_criteria_id_bfe67f05;
       public            postgres    false    209            <           1259    58204 6   admin_tools_stats_criteriatostatsm2m_stats_id_10bd79ea    INDEX     �   CREATE INDEX admin_tools_stats_criteriatostatsm2m_stats_id_10bd79ea ON public.admin_tools_stats_criteriatostatsm2m USING btree (stats_id);
 J   DROP INDEX public.admin_tools_stats_criteriatostatsm2m_stats_id_10bd79ea;
       public            postgres    false    209            =           1259    58205    auth_group_name_a6ea08ec_like    INDEX     h   CREATE INDEX auth_group_name_a6ea08ec_like ON public.auth_group USING btree (name varchar_pattern_ops);
 1   DROP INDEX public.auth_group_name_a6ea08ec_like;
       public            postgres    false    211            B           1259    58206 (   auth_group_permissions_group_id_b120cbf9    INDEX     o   CREATE INDEX auth_group_permissions_group_id_b120cbf9 ON public.auth_group_permissions USING btree (group_id);
 <   DROP INDEX public.auth_group_permissions_group_id_b120cbf9;
       public            postgres    false    213            E           1259    58207 -   auth_group_permissions_permission_id_84c5c92e    INDEX     y   CREATE INDEX auth_group_permissions_permission_id_84c5c92e ON public.auth_group_permissions USING btree (permission_id);
 A   DROP INDEX public.auth_group_permissions_permission_id_84c5c92e;
       public            postgres    false    213            H           1259    58208 (   auth_permission_content_type_id_2f476e4b    INDEX     o   CREATE INDEX auth_permission_content_type_id_2f476e4b ON public.auth_permission USING btree (content_type_id);
 <   DROP INDEX public.auth_permission_content_type_id_2f476e4b;
       public            postgres    false    215            R           1259    58209 "   auth_user_groups_group_id_97559544    INDEX     c   CREATE INDEX auth_user_groups_group_id_97559544 ON public.auth_user_groups USING btree (group_id);
 6   DROP INDEX public.auth_user_groups_group_id_97559544;
       public            postgres    false    218            U           1259    58210 !   auth_user_groups_user_id_6a12ed8b    INDEX     a   CREATE INDEX auth_user_groups_user_id_6a12ed8b ON public.auth_user_groups USING btree (user_id);
 5   DROP INDEX public.auth_user_groups_user_id_6a12ed8b;
       public            postgres    false    218            X           1259    58211 1   auth_user_user_permissions_permission_id_1fbb5f2c    INDEX     �   CREATE INDEX auth_user_user_permissions_permission_id_1fbb5f2c ON public.auth_user_user_permissions USING btree (permission_id);
 E   DROP INDEX public.auth_user_user_permissions_permission_id_1fbb5f2c;
       public            postgres    false    221            [           1259    58212 +   auth_user_user_permissions_user_id_a95ead1b    INDEX     u   CREATE INDEX auth_user_user_permissions_user_id_a95ead1b ON public.auth_user_user_permissions USING btree (user_id);
 ?   DROP INDEX public.auth_user_user_permissions_user_id_a95ead1b;
       public            postgres    false    221            O           1259    58213     auth_user_username_6821ab7c_like    INDEX     n   CREATE INDEX auth_user_username_6821ab7c_like ON public.auth_user USING btree (username varchar_pattern_ops);
 4   DROP INDEX public.auth_user_username_6821ab7c_like;
       public            postgres    false    217            ^           1259    58214 *   dash_stats_criteria_criteria_name_7fe7ae1e    INDEX     s   CREATE INDEX dash_stats_criteria_criteria_name_7fe7ae1e ON public.dash_stats_criteria USING btree (criteria_name);
 >   DROP INDEX public.dash_stats_criteria_criteria_name_7fe7ae1e;
       public            postgres    false    223            _           1259    58215 /   dash_stats_criteria_criteria_name_7fe7ae1e_like    INDEX     �   CREATE INDEX dash_stats_criteria_criteria_name_7fe7ae1e_like ON public.dash_stats_criteria USING btree (criteria_name varchar_pattern_ops);
 C   DROP INDEX public.dash_stats_criteria_criteria_name_7fe7ae1e_like;
       public            postgres    false    223            b           1259    58216 '   dashboard_stats_graph_key_4256e63f_like    INDEX     |   CREATE INDEX dashboard_stats_graph_key_4256e63f_like ON public.dashboard_stats USING btree (graph_key varchar_pattern_ops);
 ;   DROP INDEX public.dashboard_stats_graph_key_4256e63f_like;
       public            postgres    false    225            e           1259    58217 $   dashboard_stats_graph_title_99e6d271    INDEX     g   CREATE INDEX dashboard_stats_graph_title_99e6d271 ON public.dashboard_stats USING btree (graph_title);
 8   DROP INDEX public.dashboard_stats_graph_title_99e6d271;
       public            postgres    false    225            f           1259    58218 )   dashboard_stats_graph_title_99e6d271_like    INDEX     �   CREATE INDEX dashboard_stats_graph_title_99e6d271_like ON public.dashboard_stats USING btree (graph_title varchar_pattern_ops);
 =   DROP INDEX public.dashboard_stats_graph_title_99e6d271_like;
       public            postgres    false    225            i           1259    58219 )   django_admin_log_content_type_id_c4bce8eb    INDEX     q   CREATE INDEX django_admin_log_content_type_id_c4bce8eb ON public.django_admin_log USING btree (content_type_id);
 =   DROP INDEX public.django_admin_log_content_type_id_c4bce8eb;
       public            postgres    false    227            l           1259    58220 !   django_admin_log_user_id_c564eba6    INDEX     a   CREATE INDEX django_admin_log_user_id_c564eba6 ON public.django_admin_log USING btree (user_id);
 5   DROP INDEX public.django_admin_log_user_id_c564eba6;
       public            postgres    false    227            s           1259    58221 #   django_session_expire_date_a5c62663    INDEX     e   CREATE INDEX django_session_expire_date_a5c62663 ON public.django_session USING btree (expire_date);
 7   DROP INDEX public.django_session_expire_date_a5c62663;
       public            postgres    false    233            v           1259    58222 (   django_session_session_key_c0390e0f_like    INDEX     ~   CREATE INDEX django_session_session_key_c0390e0f_like ON public.django_session USING btree (session_key varchar_pattern_ops);
 <   DROP INDEX public.django_session_session_key_c0390e0f_like;
       public            postgres    false    233            w           1259    58223 .   fracas_action_defect_discussion_id_id_22ab6bd9    INDEX     {   CREATE INDEX fracas_action_defect_discussion_id_id_22ab6bd9 ON public.fracas_action USING btree (defect_discussion_id_id);
 B   DROP INDEX public.fracas_action_defect_discussion_id_id_22ab6bd9;
       public            postgres    false    234            z           1259    58224 *   fracas_asset_asset_config_id_1b7bf1fc_like    INDEX     �   CREATE INDEX fracas_asset_asset_config_id_1b7bf1fc_like ON public.fracas_asset USING btree (asset_config_id varchar_pattern_ops);
 >   DROP INDEX public.fracas_asset_asset_config_id_1b7bf1fc_like;
       public            postgres    false    236            �           1259    58225 *   fracas_correctiveaction_defect_id_6b07c98b    INDEX     s   CREATE INDEX fracas_correctiveaction_defect_id_6b07c98b ON public.fracas_correctiveaction USING btree (defect_id);
 >   DROP INDEX public.fracas_correctiveaction_defect_id_6b07c98b;
       public            postgres    false    240            �           1259    58226 >   fracas_defectdiscussion_attendees_defectdiscussion_id_68582c3b    INDEX     �   CREATE INDEX fracas_defectdiscussion_attendees_defectdiscussion_id_68582c3b ON public.fracas_defectdiscussion_attendees USING btree (defectdiscussion_id);
 R   DROP INDEX public.fracas_defectdiscussion_attendees_defectdiscussion_id_68582c3b;
       public            postgres    false    245            �           1259    58227 <   fracas_defectdiscussion_attendees_employeemaster_id_97632480    INDEX     �   CREATE INDEX fracas_defectdiscussion_attendees_employeemaster_id_97632480 ON public.fracas_defectdiscussion_attendees USING btree (userprofile_id);
 P   DROP INDEX public.fracas_defectdiscussion_attendees_employeemaster_id_97632480;
       public            postgres    false    245            �           1259    58228 *   fracas_defectdiscussion_defect_id_777a85b9    INDEX     s   CREATE INDEX fracas_defectdiscussion_defect_id_777a85b9 ON public.fracas_defectdiscussion USING btree (defect_id);
 >   DROP INDEX public.fracas_defectdiscussion_defect_id_777a85b9;
       public            postgres    false    244            �           1259    58229 0   fracas_defectdiscussion_review_board_id_30bd7f7d    INDEX        CREATE INDEX fracas_defectdiscussion_review_board_id_30bd7f7d ON public.fracas_defectdiscussion USING btree (review_board_id);
 D   DROP INDEX public.fracas_defectdiscussion_review_board_id_30bd7f7d;
       public            postgres    false    244            �           1259    58230 .   fracas_failuredata_asset_config_id_id_411469d0    INDEX     {   CREATE INDEX fracas_failuredata_asset_config_id_id_411469d0 ON public.fracas_failuredata USING btree (asset_config_id_id);
 B   DROP INDEX public.fracas_failuredata_asset_config_id_id_411469d0;
       public            postgres    false    250            �           1259    58231 3   fracas_failuredata_asset_config_id_id_411469d0_like    INDEX     �   CREATE INDEX fracas_failuredata_asset_config_id_id_411469d0_like ON public.fracas_failuredata USING btree (asset_config_id_id varchar_pattern_ops);
 G   DROP INDEX public.fracas_failuredata_asset_config_id_id_411469d0_like;
       public            postgres    false    250            �           1259    58232 %   fracas_failuredata_defect_id_45343e26    INDEX     i   CREATE INDEX fracas_failuredata_defect_id_45343e26 ON public.fracas_failuredata USING btree (defect_id);
 9   DROP INDEX public.fracas_failuredata_defect_id_45343e26;
       public            postgres    false    250            �           1259    58233 &   fracas_failuredata_mode_id_id_32b9227b    INDEX     k   CREATE INDEX fracas_failuredata_mode_id_id_32b9227b ON public.fracas_failuredata USING btree (mode_id_id);
 :   DROP INDEX public.fracas_failuredata_mode_id_id_32b9227b;
       public            postgres    false    250            �           1259    58234 (   fracas_failuremode_mode_id_68d1dc4e_like    INDEX     ~   CREATE INDEX fracas_failuremode_mode_id_68d1dc4e_like ON public.fracas_failuremode USING btree (mode_id varchar_pattern_ops);
 <   DROP INDEX public.fracas_failuremode_mode_id_68d1dc4e_like;
       public            postgres    false    252            �           1259    58235    fracas_history_user_id_508829c0    INDEX     ]   CREATE INDEX fracas_history_user_id_508829c0 ON public.fracas_history USING btree (user_id);
 3   DROP INDEX public.fracas_history_user_id_508829c0;
       public            postgres    false    254            �           1259    58236 $   fracas_pbsmaster_project_id_967c21df    INDEX     g   CREATE INDEX fracas_pbsmaster_project_id_967c21df ON public.fracas_pbsmaster USING btree (project_id);
 8   DROP INDEX public.fracas_pbsmaster_project_id_967c21df;
       public            postgres    false    256            �           1259    58237 #   fracas_rootcause_defect_id_d3f53143    INDEX     e   CREATE INDEX fracas_rootcause_defect_id_d3f53143 ON public.fracas_rootcause USING btree (defect_id);
 7   DROP INDEX public.fracas_rootcause_defect_id_d3f53143;
       public            postgres    false    264            �           1259    58393 "   fracas_systems_project_id_6f83b733    INDEX     c   CREATE INDEX fracas_systems_project_id_6f83b733 ON public.fracas_systems USING btree (project_id);
 6   DROP INDEX public.fracas_systems_project_id_6f83b733;
       public            postgres    false    281            �           1259    58238 )   fracas_userprofile_product_id_id_b5877d4c    INDEX     q   CREATE INDEX fracas_userprofile_product_id_id_b5877d4c ON public.fracas_userprofile USING btree (product_id_id);
 =   DROP INDEX public.fracas_userprofile_product_id_id_b5877d4c;
       public            postgres    false    277            �           1259    58239 #   fracas_userprofile_user_id_a6d557eb    INDEX     e   CREATE INDEX fracas_userprofile_user_id_a6d557eb ON public.fracas_userprofile USING btree (user_id);
 7   DROP INDEX public.fracas_userprofile_user_id_a6d557eb;
       public            postgres    false    277            �           1259    58240 (   fracas_userprofile_user_type_id_c66bfd15    INDEX     o   CREATE INDEX fracas_userprofile_user_type_id_c66bfd15 ON public.fracas_userprofile USING btree (user_role_id);
 <   DROP INDEX public.fracas_userprofile_user_type_id_c66bfd15;
       public            postgres    false    277            �           1259    58241     fracas_userresetkey_key_1d7664f0    INDEX     _   CREATE INDEX fracas_userresetkey_key_1d7664f0 ON public.fracas_userresetkey USING btree (key);
 4   DROP INDEX public.fracas_userresetkey_key_1d7664f0;
       public            postgres    false    279            �           1259    58242 %   fracas_userresetkey_key_1d7664f0_like    INDEX     x   CREATE INDEX fracas_userresetkey_key_1d7664f0_like ON public.fracas_userresetkey USING btree (key varchar_pattern_ops);
 9   DROP INDEX public.fracas_userresetkey_key_1d7664f0_like;
       public            postgres    false    279            �           1259    58243 $   fracas_userresetkey_user_id_499fbb9d    INDEX     g   CREATE INDEX fracas_userresetkey_user_id_499fbb9d ON public.fracas_userresetkey USING btree (user_id);
 8   DROP INDEX public.fracas_userresetkey_user_id_499fbb9d;
       public            postgres    false    279            �           2606    58244 [   admin_tools_stats_criteriatostatsm2m admin_tools_stats_cr_criteria_id_bfe67f05_fk_dash_stat    FK CONSTRAINT     �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_cr_criteria_id_bfe67f05_fk_dash_stat FOREIGN KEY (criteria_id) REFERENCES public.dash_stats_criteria(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m DROP CONSTRAINT admin_tools_stats_cr_criteria_id_bfe67f05_fk_dash_stat;
       public          postgres    false    223    3425    209            �           2606    58249 X   admin_tools_stats_criteriatostatsm2m admin_tools_stats_cr_stats_id_10bd79ea_fk_dashboard    FK CONSTRAINT     �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m
    ADD CONSTRAINT admin_tools_stats_cr_stats_id_10bd79ea_fk_dashboard FOREIGN KEY (stats_id) REFERENCES public.dashboard_stats(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.admin_tools_stats_criteriatostatsm2m DROP CONSTRAINT admin_tools_stats_cr_stats_id_10bd79ea_fk_dashboard;
       public          postgres    false    225    3432    209            �           2606    58254 O   auth_group_permissions auth_group_permissio_permission_id_84c5c92e_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissio_permission_id_84c5c92e_fk_auth_perm;
       public          postgres    false    215    213    3404            �           2606    58259 P   auth_group_permissions auth_group_permissions_group_id_b120cbf9_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_group_permissions
    ADD CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 z   ALTER TABLE ONLY public.auth_group_permissions DROP CONSTRAINT auth_group_permissions_group_id_b120cbf9_fk_auth_group_id;
       public          postgres    false    213    211    3393            �           2606    58264 E   auth_permission auth_permission_content_type_id_2f476e4b_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_permission
    ADD CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.auth_permission DROP CONSTRAINT auth_permission_content_type_id_2f476e4b_fk_django_co;
       public          postgres    false    3440    215    229            �           2606    58269 D   auth_user_groups auth_user_groups_group_id_97559544_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id FOREIGN KEY (group_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 n   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_group_id_97559544_fk_auth_group_id;
       public          postgres    false    3393    218    211            �           2606    58274 B   auth_user_groups auth_user_groups_user_id_6a12ed8b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_groups
    ADD CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.auth_user_groups DROP CONSTRAINT auth_user_groups_user_id_6a12ed8b_fk_auth_user_id;
       public          postgres    false    217    218    3406            �           2606    58279 S   auth_user_user_permissions auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm FOREIGN KEY (permission_id) REFERENCES public.auth_permission(id) DEFERRABLE INITIALLY DEFERRED;
 }   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm;
       public          postgres    false    215    221    3404            �           2606    58284 V   auth_user_user_permissions auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.auth_user_user_permissions
    ADD CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.auth_user_user_permissions DROP CONSTRAINT auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id;
       public          postgres    false    217    3406    221            �           2606    58289 G   django_admin_log django_admin_log_content_type_id_c4bce8eb_fk_django_co    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co FOREIGN KEY (content_type_id) REFERENCES public.django_content_type(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_content_type_id_c4bce8eb_fk_django_co;
       public          postgres    false    227    229    3440            �           2606    58294 B   django_admin_log django_admin_log_user_id_c564eba6_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.django_admin_log
    ADD CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.django_admin_log DROP CONSTRAINT django_admin_log_user_id_c564eba6_fk_auth_user_id;
       public          postgres    false    227    3406    217            �           2606    58299 F   fracas_action fracas_action_defect_discussion_id_22ab6bd9_fk_fracas_de    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_action
    ADD CONSTRAINT fracas_action_defect_discussion_id_22ab6bd9_fk_fracas_de FOREIGN KEY (defect_discussion_id_id) REFERENCES public.fracas_defectdiscussion(defect_discussion_id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.fracas_action DROP CONSTRAINT fracas_action_defect_discussion_id_22ab6bd9_fk_fracas_de;
       public          postgres    false    234    3464    244            �           2606    58304 L   fracas_correctiveaction fracas_correctiveact_defect_id_6b07c98b_fk_fracas_de    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_correctiveaction
    ADD CONSTRAINT fracas_correctiveact_defect_id_6b07c98b_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.fracas_correctiveaction DROP CONSTRAINT fracas_correctiveact_defect_id_6b07c98b_fk_fracas_de;
       public          postgres    false    240    3461    242            �           2606    58309 L   fracas_defectdiscussion fracas_defectdiscuss_defect_id_777a85b9_fk_fracas_de    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscuss_defect_id_777a85b9_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.fracas_defectdiscussion DROP CONSTRAINT fracas_defectdiscuss_defect_id_777a85b9_fk_fracas_de;
       public          postgres    false    244    3461    242            �           2606    58314 `   fracas_defectdiscussion_attendees fracas_defectdiscuss_defectdiscussion_id_68582c3b_fk_fracas_de    FK CONSTRAINT       ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscuss_defectdiscussion_id_68582c3b_fk_fracas_de FOREIGN KEY (defectdiscussion_id) REFERENCES public.fracas_defectdiscussion(defect_discussion_id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees DROP CONSTRAINT fracas_defectdiscuss_defectdiscussion_id_68582c3b_fk_fracas_de;
       public          postgres    false    245    3464    244            �           2606    58319 R   fracas_defectdiscussion fracas_defectdiscuss_review_board_id_30bd7f7d_fk_fracas_re    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion
    ADD CONSTRAINT fracas_defectdiscuss_review_board_id_30bd7f7d_fk_fracas_re FOREIGN KEY (review_board_id) REFERENCES public.fracas_reviewboard(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.fracas_defectdiscussion DROP CONSTRAINT fracas_defectdiscuss_review_board_id_30bd7f7d_fk_fracas_re;
       public          postgres    false    244    3496    262            �           2606    58324 [   fracas_defectdiscussion_attendees fracas_defectdiscuss_userprofile_id_40c62480_fk_fracas_us    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees
    ADD CONSTRAINT fracas_defectdiscuss_userprofile_id_40c62480_fk_fracas_us FOREIGN KEY (userprofile_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;
 �   ALTER TABLE ONLY public.fracas_defectdiscussion_attendees DROP CONSTRAINT fracas_defectdiscuss_userprofile_id_40c62480_fk_fracas_us;
       public          postgres    false    245    3511    277            �           2606    58329 N   fracas_failuredata fracas_failuredata_asset_config_id_id_411469d0_fk_fracas_as    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_asset_config_id_id_411469d0_fk_fracas_as FOREIGN KEY (asset_config_id_id) REFERENCES public.fracas_asset(asset_config_id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.fracas_failuredata DROP CONSTRAINT fracas_failuredata_asset_config_id_id_411469d0_fk_fracas_as;
       public          postgres    false    250    236    3452            �           2606    58334 E   fracas_failuredata fracas_failuredata_defect_id_45343e26_fk_fracas_de    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_defect_id_45343e26_fk_fracas_de FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;
 o   ALTER TABLE ONLY public.fracas_failuredata DROP CONSTRAINT fracas_failuredata_defect_id_45343e26_fk_fracas_de;
       public          postgres    false    250    242    3461            �           2606    58339 R   fracas_failuredata fracas_failuredata_mode_id_id_32b9227b_fk_fracas_failuremode_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_failuredata
    ADD CONSTRAINT fracas_failuredata_mode_id_id_32b9227b_fk_fracas_failuremode_id FOREIGN KEY (mode_id_id) REFERENCES public.fracas_failuremode(id) DEFERRABLE INITIALLY DEFERRED;
 |   ALTER TABLE ONLY public.fracas_failuredata DROP CONSTRAINT fracas_failuredata_mode_id_id_32b9227b_fk_fracas_failuremode_id;
       public          postgres    false    250    3484    252            �           2606    58344 G   fracas_history fracas_history_user_id_508829c0_fk_fracas_userprofile_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_history
    ADD CONSTRAINT fracas_history_user_id_508829c0_fk_fracas_userprofile_id FOREIGN KEY (user_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;
 q   ALTER TABLE ONLY public.fracas_history DROP CONSTRAINT fracas_history_user_id_508829c0_fk_fracas_userprofile_id;
       public          postgres    false    254    3511    277            �           2606    58349 B   fracas_pbsmaster fracas_pbsmaster_project_id_967c21df_fk_fracas_pr    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_pbsmaster
    ADD CONSTRAINT fracas_pbsmaster_project_id_967c21df_fk_fracas_pr FOREIGN KEY (project_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;
 l   ALTER TABLE ONLY public.fracas_pbsmaster DROP CONSTRAINT fracas_pbsmaster_project_id_967c21df_fk_fracas_pr;
       public          postgres    false    256    3494    260            �           2606    58354 O   fracas_rootcause fracas_rootcause_defect_id_d3f53143_fk_fracas_defect_defect_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_rootcause
    ADD CONSTRAINT fracas_rootcause_defect_id_d3f53143_fk_fracas_defect_defect_id FOREIGN KEY (defect_id) REFERENCES public.fracas_defect(defect_id) DEFERRABLE INITIALLY DEFERRED;
 y   ALTER TABLE ONLY public.fracas_rootcause DROP CONSTRAINT fracas_rootcause_defect_id_d3f53143_fk_fracas_defect_defect_id;
       public          postgres    false    264    3461    242            �           2606    58388 N   fracas_systems fracas_systems_project_id_6f83b733_fk_fracas_product_product_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_systems
    ADD CONSTRAINT fracas_systems_project_id_6f83b733_fk_fracas_product_product_id FOREIGN KEY (project_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;
 x   ALTER TABLE ONLY public.fracas_systems DROP CONSTRAINT fracas_systems_project_id_6f83b733_fk_fracas_product_product_id;
       public          postgres    false    281    3494    260            �           2606    58359 I   fracas_userprofile fracas_userprofile_product_id_id_b5877d4c_fk_fracas_pr    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_product_id_id_b5877d4c_fk_fracas_pr FOREIGN KEY (product_id_id) REFERENCES public.fracas_product(product_id) DEFERRABLE INITIALLY DEFERRED;
 s   ALTER TABLE ONLY public.fracas_userprofile DROP CONSTRAINT fracas_userprofile_product_id_id_b5877d4c_fk_fracas_pr;
       public          postgres    false    277    3494    260            �           2606    58364 F   fracas_userprofile fracas_userprofile_user_id_a6d557eb_fk_auth_user_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_user_id_a6d557eb_fk_auth_user_id FOREIGN KEY (user_id) REFERENCES public.auth_user(id) DEFERRABLE INITIALLY DEFERRED;
 p   ALTER TABLE ONLY public.fracas_userprofile DROP CONSTRAINT fracas_userprofile_user_id_a6d557eb_fk_auth_user_id;
       public          postgres    false    277    3406    217            �           2606    58369 L   fracas_userprofile fracas_userprofile_user_role_id_9082133f_fk_auth_group_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_userprofile
    ADD CONSTRAINT fracas_userprofile_user_role_id_9082133f_fk_auth_group_id FOREIGN KEY (user_role_id) REFERENCES public.auth_group(id) DEFERRABLE INITIALLY DEFERRED;
 v   ALTER TABLE ONLY public.fracas_userprofile DROP CONSTRAINT fracas_userprofile_user_role_id_9082133f_fk_auth_group_id;
       public          postgres    false    277    3393    211            �           2606    58374 Q   fracas_userresetkey fracas_userresetkey_user_id_499fbb9d_fk_fracas_userprofile_id    FK CONSTRAINT     �   ALTER TABLE ONLY public.fracas_userresetkey
    ADD CONSTRAINT fracas_userresetkey_user_id_499fbb9d_fk_fracas_userprofile_id FOREIGN KEY (user_id) REFERENCES public.fracas_userprofile(id) DEFERRABLE INITIALLY DEFERRED;
 {   ALTER TABLE ONLY public.fracas_userresetkey DROP CONSTRAINT fracas_userresetkey_user_id_499fbb9d_fk_fracas_userprofile_id;
       public          postgres    false    279    3511    277            j      x������ � �      l   Q   x�3�.-H-RpL����2��
>�e�9\ƜA��
�y�y��E\&�e���P9SN��Ē�".3N��̼ *����� _��      n      x������ � �      p   J  x�}�[��8���UdS87�y�1UT���S�Jb��ز%������/d�_�A���G5�c5���<,c�nö
%��%��EY[��;<~tF�6bQcE���-'r����?��/#ٗcAW:Iu]�M/� �̑���?��Ȟ1D9~8+��=t�r*���T!D8�j��j�!Ľ��Ɩ��m��1RhJb(BN�hJz8~N_��Kj{�	���?�~l�[�����>J���Q΄dGOBI��s����c�������M�:�	R�Lsd0$I���i2��IA2�Y��S�6I���Y��� ���� !���M��ͯU/�h���53*���;�y �p{���h�I�3?6��U������-�+��N�7�38�Ay�N;Po����z�	ÓlصG���Az#!�U@��7a˞�}����l�aw;0��cZr�a�}�ɣ��W��5�$[�B�o�@�7X�|����4x�����Ztu�G-�{1�ھ$[v�c�cv�cd��1n�f�9�|�A��f�/�����<s'P�̽�g�u���i�n����|�s��?�Ϊ\�7ܺ�Zn�.<�v��i�z,���3B�},C�-�U��42�܋e_��c��$���{���	9j& �q����P������1c��K̣���LĮ1��p��j����u>u$-�eߧ�%ұ>C�Ǵ�DR�|����HH:�����s�<�eGfkD|��y)ߴ�"FƵm е����om�Ӱ��O(�b��nU�c3�3�1�fd�x,#N͈�Ib	���V��hV<Ƨ?F��a>�1؏>�鏡n�C]�OD�s�����
C,�siL��,�Kc҂��4���`>5[���W�E]����Y��d���>j�ْk�	P��\�<q�>��gr�U�#�_�gn�DAg*q�&":d���6��ԅt���Ɨ��j�ƅGyf�%���c>%���#�$���A'nƤ|���ksߠSę�2+��%�hV	g���@��c�2��wن���L��l�>2�5�������0M|�|r�l��W!$�"��U���^�c\�0}�.i��4I�c�:i��@I�S�Fi��LI�s�R��;Ņb׏���)JZ$H*�J����$a��� M�2�\���s�0vۄh����u��ā����le�0��� �O���m��@q��Z�R�J�m!P�2.P}�X�T����l^ޢqC<��ZB�Idݔ�pI�$��!��,�zL�hj?�a�b8��z%q
�4*��(�B��4��*7���T��7B��Ⱥ�OZ$]�`�G-���KJ�?:ʺ�      r   �  x���Ys�H�k�+r��%�n�N�1q7`\�V�j
Y�E�`�D�)39\pAA���o�T�+�r�_�k �$ @�Hfw=���H
��X�W%�sw�1�m�i�ƶ��Q+��u��~on����+N���q���u`x[��Jq9��� �5kH<B�EB&�aD���T�Cq�����X�,�-5�l�\}"�yϞtrӮg�S��o:�;����}>���Z�TQ!��ߋ:�I|��*TdD)e����`!�gm2g��q%�.���8P�	���7�t�9�-(Y����2�XT��#�*�*�2��)���i%1���}���� S ������jz�X";K��48�K�5�)��w��iZݧ��kЫ�W����~��5?��`�G��T��0��5�K��m�L�LƔ3Xz��e�@\ߵLz��E8{��hVaY-޴\��;V�h��w3����?K/���%$� FW��K���>��� ��^?*�*F���D��S�~���7d"�Mѝ��CN���6�T,I8�ǉ��ԧ�`��,��>�"�$S��R��7⻹^���x��B�o��(�O���:���6MM�"/!�ݦ���i�dK-R5�u��x��as��o��fR!��	+�`�q���A+z�)�B)����D����6��i�l��������%�b�2��e�i�8����^.�b*P!*�Bbܟ
7���e�`A.��up����U�1ɪyݩ;��ڸڶ���1�s�7�P;l�p���tA�O+����
/�S�Q������� #�/{����NS�&������ߺ�׳��"������;��+}��F�$��K�ɲ��~��2������6V�go���pY�_��~ф��5�߲x�;�y���-w�t�������`w:��it����L g8�f�/��q��t�J�� �\G��N����yJd&'�A�%?<<�J�{      s      x������ � �      v      x������ � �      x      x������ � �      z      x������ � �      |      x������ � �      ~   K  x��R�n�0�?�Ԅ~��$��F#٦o���N�����w>�ʺ��Zb�f���Y���%7�`��4��[�^PsS�\`��T/�M�Sv����g�����\(��bd$8�&���d����<���F�d��2��ֹv�b� ����n$�!���X�ی6�(M������r�b��&���Û��9/Їg�s3>�����S0]���&�r�p挕��9[�!�F	S8���r!��eI91-pc
Ȕ�$�X�a��N-��a��I�E���0��߂��'���z�X��Ƽ�*�\�jL?\eV���J"<%g��� � [:�      �   <  x����n�<��;W���"E�'ײ��i�N�I����׻_ʉ%:V0]��A[=��W/I�������^._�~|1�@��/����᧡�^���@�����֚l^����7VY��Ϋ�����XF�87/ú���!A_i菧?}�8N����@3�V��Y���������Gz�}ڿIB�8p�э�.��aL㥻|'��!��m�v���hmZt��Lsm��40�'��Z4J�|Fi׍���a7�,}����?��4��lpgnhsye�2��m:�%��Ms˖��4�,Og�0� ��x#��`u�p���)�&}vǾ�cq>\��Ɖ:�~H�~8��1+73ұ�'����&��g�:[p�����?v���I���v:*$Ҥ�m
�t��o�cIk̡/��ʱ|^�;E187׹r���^�CI�t)���a�,�������]w9���0��t�Ǳ�xb��\9�P�������-?+����|}�F!�L�����i��z�Ɂ�y�
	��,���y8����$W��8��Ǘ��{�����^�}����u���|"�O,�`CGJ2���-`F��x�g��DLƂo X,�V�y����6^�^�إn��e�1��+��z!mC(�� Q�B��@[�-[9H�Iho��G�y#�� �b3K����f�Wy9O��`�5B�MA ���
���T(�{$0�A6�Ɖ�֫�}:��r���ǩs��W�ʡR��
��>�*FXD��M��� 	aa�wX6��r8���.�� [[�Md�Rقf���ӥ�ɷ����4X��ƚb�A	S���.d�p[csB`��D)���ǳ�w]��Ar���Q��\��R$,	.���o�g-���4\A)��䀡"BNNQ �P�)*E��w���{��	Cr*a���|�Q����Y�Pq��J����F�K��?;�!���#�XFT���,s�I\�����d��ѨT)�	"l45�8	��֊g���+*u�Y!�:� ����N��B!ݚ)�dT�D|D�~@� �d����v�@l"b6��(J�ݿ�o��~|�NE��1]� ��W^G�<�J!﷌\F0J��V��|���LTJ���j2�]bkC�Ú����ơ*u�1�i��C��\ 
H�ԮtJ����"��X%T�*�i3�0�0�R-�7��Ƿa�#m�����Q��V��������W�5UxJ���Y���`F�Ҳ]i��Q�R|M��`�?)�ڑ����óV��KS#��E�\4	J��MΟ.ݯC����i���i�	���3k;={Y,�mIɲ�܀V�QW�o�$P&y�����(���7�T��Fm���:�[�2��,���k$���9�]�����"�\$�5�-�z\J�dt8�z��Dǖjj��	c���`�2{?7@򧊁Ob�OM��뫍��U���rj��ayub���C�h�FX�x��MP��!�`�]?�烨��tb�5gʾɥ߲�4|��O2n�E��Pi��=�-���𖤓�R���0��)<2���t�2����q(qS\1J9�V0��;A��$T�f������Lq�m�x�	 ��*]3���*�����4�$W�J̌��!��7����ҌcQ�U��^�)�s�6�*b6y�͞eC2��P��*�2���T��G阸��I(k��Kb4�0`ꃥ�� =���h�*��{d�qO#�߀G�[Q�d�B�zP��0�旜�X�L+?F!$�g�7�*ar\ �`�`T���37�FP�qa(a:�``~M��A���E^���P�t�`؄�Gm1���N�d��b����+�OJ�ή��Δ�% %RGk�1@m�I����k��=_͏�H�R�R�sW��)�Da!g�H��J�R�2D[�6Cz�P4FJ�n)Ә�6C�`U�I���G!-�E����+B��/d*f�����-��w�%S�@�_?o�U���ט�Z+�zL��H���W��-lL��0#��|�?��Wa�=�Oc'���mz"��d�Y���e��zL��t����v��t�	�K FO��ߛ?~����      �      x��}Wo����uΧ���SY�/l�X�IE��I���E��ۧg˛��=k�7U@�XV��=��3���Ȏ�w����'����i�X�����#��B}7F�hi�F�^��*Vz����=ZB}m�Zj0� g������=�����1vK�Ϻ����h�����jdE����\��p|}�zfl׷�Z�ɪ3v�J���>���j�Ud�瞆�Ȍ�����9�n"Cm�{�yr�w��($�h�`���Q�c���P�iDA+_	�N]{��R���NU���{� �}�� <�p ��_@��V�l��&U!Yu���v�Q6nu����!�G
R��V�P��H�M�{m����*���-k")XY?����}Nrm=&�����j�ը���:��ݒ�����6�v�h�� J<����Ay��!*��L�¨����N�J�S��7�}�F����>4D��G����*�{�R��z��N�6��Q1��;=�C�u@��%\z�ZkԩB���h�21�3b_(=�@�����o �P�n}�_�h,�a��f�����r�+=�]YGL1��'�ϰ�3|�7(Ba�%,A����I�� {��JZe�rɾİ��w�(���Qp��j����,[}:a�oF��ֲ���H���btA����o _��ګ�I���x�[LZ���%X�Z����u�N��`~�C(�	O�uM����ڭs0�uU'N�eRQ���{�#|�o!C �2~@��\"F���0茼pAh{�����,��=3�{ �G�HC�Rfz�+�t�셦�/,�*�˘�m�G� ���;�Ǭ.4���dx-+u߷�}�����wUY4��3�q� <��,�4�<p��n�mh �)"�1�>ME�r�A)��;�G�2�����&qMY�4�</��Cgے�AP��3|�A0D��$�������o�$�����ܲ��6ԡ��#|L��z,lc�C��_�Ӽ��9��Eane�$�)��I��}��� fy� ɒ$��fډi�#(�Y�N[�U(�؇���\��>�A�จK��q�=@�2�{r�:�}jtq[㚖�8�}>�=�!/��)<%\\1<Ž��7�d�E_�AT�v����#|�o�a�A�S�&G6��>��Ե�4؃(��+5	�|��g�8|s�KC, ���>�'��Te���>67KAΥ���C���x���x̖�!����y��g5���V�tf";F5��s�v���Qĳ�D�!=q�]�Q����N_9�LH�%{#��}l������UDB: �P��d��0�d�0RӪ,�r���ϠӼ��0jA%XR5�Q�S��u��P!-��XY��<f�7��?��G�e�u�Xݍ;m�#[0�ѧJ������SF
Y�K��'��R.�dQ��_�	tEI8�ՆYR��,Ǒ�ʐr�����~�� s\$$�R]e��Q��SʹI����'�>jT�)�#|��6��
I� &�1'0�c�wS��ԬZW���	5Ӧ9;.>��� ���y{Y!�ɩAZ�ql7i��<��Ⴠ�ǌ/3P	9E]#K&����L!�,�8{��(��+pg���Q�q��s�f'(}�6V8����f�a������J�gn�z����(V�,Ԟ�-��Wlc-P��n���M��Z��1d� Zp��m����Cb�(�wm��{���Gͩ�;�Cz`%������L����6��Ј'���JCre_�SͧG��Ƨ׭����t[,�I`�m�>�xB��7��9�k���l�#�zƼ	���ҩ�M�K|LA �S�Z���� ��Cĳ4X<F*"��	r��P��=��z�!%VR��3�+�w�#;�}��(��fsC����b4������*b�x���H�D���|_Ǐ�j�u�;��������H�cd��ZGQ��������3o`���G1E�O��(���}A�($a!Q���T���Z��h���'���Xۑ�[dF�^]_P����z�0��k/V�ˏ>�'�m]o;;s(
٩�3�aڻ����p�_�<��f�*�v41;��+��ۘ�ϭ_w�T�2��z$�S2�{�p���e�Ō��%d�4e��+��^�D��^A��1��f��Xl1S��3�GvE6M4���G�d��{(�{�rvvdul�Qi޳=ߣ�g�v�ݶ��$ѷ�;J�)��c�q�x��;���l5���ͱ�)�vwy��m�a�Z�W�ZۭJ�)j=�7�o��X���5����3���&�Ll�{�Y3�.;8]��nM���u���$�]۞�]>�~��PC/��6�R�;j�"P� �ʙŴ�=��y���b8�����4�v�E��ym�����q���8���֛M�N�i�qM���S�xD�-FG�^��X����qz��V�1b��������Ϗ?>?�ʾ��k���v�t���=}�~u��繧��ǽ�cZ��GO��yV�IT�o�>t�
I��K����h�_2�kk��{���r)�Q/DCB"(K"6]Ih��+��(A�Y�8"�;�v̀�z�l�|-а�o�1��bm���n/�^��j�w}5�'"f�QnL��/2�70c����ۛ������bǌc0	Yx(�%`F�Qz����1-���`P3��Аg���">�x���V\�S.���#+�z��]T6��S���{�E�V�$,vL�"�7�5�}ZL7L�'�Dc}=g��g�,�z��'�G-��fJ����(�]cdb,3�=����/F*s�f�ER䞯�����4���O��&%�#<��ȏ�O"ˉ)��HHNҺL��IE�q�Tpjpv�^�q����� K2=)������A�")��,}Z�g�_9z/5 aH� K�'�=)�l�A(�.kA��!���XĎ��3r��̥��BffXl�_��c�ǄM.=e���~i�_�5:)�?`��TPH�cc�1eԻ�:�$�v�B��/�uv���r6��ቨ!`fRf�����M�I�*b[A¹����h�DBs ��9f��B�,�Lf�$Qۇ2@U�4��F>4�@dL-A>C�Zȑ�+�<��<��ؚ�Iuf"9�9�,G����.kH_c�	�wF���� �4G\B0`�Z�<+����Q��$�M�^�|@
`�c�g���XC�5��u�*=���Y��jk�A�3;ʓ
�x�In��;>�~v�L[o�b}y��cn�CV>��t�̈:R����Z��ʈy�K��y��h���n�/Fc�p
��`���#���q��!�yL��^]��10�>I���ҋig:uX7��_��w����ʲO����4J�PTKf�E`��,�*Wr��!5䄧RX|�@"?v�XU�&>�{�V=�m��(KC���
�g�_�pLc�o 1E�uK;��}��!r3u�H�+O���t��u�����^�@�2y��$�<!y����F,�N/6X=������5��D�$t
�,�F�a]E���������*J�T^:�	oV��Vw����d�P�VwK��إ2r�ߕF~M��:��
_�����S�b�<=qwy�H�c׸�Gz �{��[4	�]T�"��zV'�k�~}|�ԩ�'Ղ]�����H��/���������jn�NJ�'�1 |R�c�](wM�޵��Ձ�=dK��勪ZLc}���~��"��Sv��|��`�.��%`�ٔF��][q�r�6yuk!�~Eg�	�]�P�H���k3xi%����gS���.#}���g�0��ٔ�<��m�h{��$���y{��t�������Ųgū��,H�s?|�<E�G絗CZY`�V�u�ڢ�O�Щ�wj`1ӱ
�>�q/�V[V���cu:a�"��]tj�*�����/jտ#�.Fn�D|c�?��٭��X��}h��C�津���nb��	�mh�/]���[3q���'l�T=uL�0�~(��D1/گ��bt�j�"�w���E}�3��fW.{�3��_y�?����?���Õ�}�N/]�    ��Tj���W3;�f�����h�G^yhP��^�ۍ&��y����O~<Y�_ ��w#�o�`��'2�=�U����ݽ)�f�}��g������,�/�~*���}s���g�Φ+&;[��W����g'�O*m�RE�?�B�~�2�;���rX]/��_��a��?�t�Y^��0��[+k��=��j�n�y��N��ۆ�c�m����x�ގ��x�}�·�{�S���l�J]���;�o��Xyj6�H����|���M�`ȻT� A|���Q�I�e��A{��{�i���\Dy]��U>�P�E(�N�Ar�q����!��}Kr��P�~!�&y��hH�<u�`]_ }�'��%֠��Z�Y�
�hi�#���(��p�.ܞfTgH��q�����,JQ�v~iW��i�=�'�Rć�L ,�$f���I]a���*��ڴ�����x�a��z֩�3H��+��Qi�2ҽ�N���KǸa$�>����u����@�O�u>����m��&^=��0*���1_"fl�Z�c�G�ls��pw��~o1���;�p���o�}�?��x�l�����j6�Y���]�qր��}��H+�f���|��{�s��'��������[�1o���^��~�0ݏ�w���۳{_��T{���?��P~�����sհ�f�?n^�1��ym�L^�Y���'�]-����)�u�뗯�?�?�Y8�#bc !yl�0{ڇ����A��<¡�'~paF�y���A�2:N���$��)7b�V.�i�At���HT�\�z`�g�_�Ǳ��qhȂ��u9QM�L�,��S���b��=�U���WC���N�s�(��1�S�}d�%J43��k�Rr�Iʼ��Y�XL��b�uZ�4�n�)��c����ddp���<}4f�dC�?��kB������V��߷�c����7���ݿ__�?[��}A��}���7}t�0�W�����s~c�u��}9�5?���&{���u�Zk�X[�h��|]����f�^��_ל�W�x/a1A�x
8�������!1NJQxh�� �;=Xvz<���?�#>�����J��c��5�{���U�%��:�����g��h��M}oO�����o1|-��,_�$���|�>}��X�zE
奦�����K�t���L��	�c;��T�r����T�7/w�^�^����~��E��[=a��3_H{]^m��gjF/w�^�&���{�G���TՇ����  }�j��V�V ����Q� ����-P@靾V�A���k�]�W{�;���x�æW�3��3�3�>���n�������������sf���<`܆�L<��و�D��<�ѯ.����ѧ�c,���$6o�Y��QqO��vB|�9� �g&D������$��̦k]z  �X�ξ�:�3���#{]�3���K"1�� J蔖�$��������h��Û��J�Z�P��x�r:F�n�*#�y�i���#4��SМ9kZˤ�]L7�:���/
�w�#{�?�|������ӳ*�ڥJ?���y�o�������g8�d���jԳ��>�&{�q�@������)?�Yۿ?О����o��������������*?�}��,Y��f�ݞyd��r��{Lހ��'�w��o�#��S9�G�$���t�N 	S|J��V���vMU7N��aB� ;�E�=�ki;~�Y��B��G�r�%ј멏�`���j�y���Ck�B�z.����@8$�!�D8�A��9��nA��C�X$�,<d���~�G���|�/ �����>?��r*�İ1��BT�g�_��p�D�D��������s;�-iشyV:ys�6v����wZ���Z����o�U�3�OgH�gL��P��x�̇��0ݲʱ��ׄ��H)-�N�{6[�?[����^�����,\a.���൪�h��[���`��h��YǛ���:s�>�y>��l��Ɵ��7;
��R�i/}�Tr�4崝�ked�hch��2�1����5�7Ol����ݦ���힓7�u�)g��f��}����_������4A��Ll]��m1��j�~>\��/�?M/	��:��S����{ц�\4MI {�=!Y�`�G���݀�l�w�0� S*
��^:7�#j���I{����CZ�h�G�^�؀���CDX��w��U��4�:$˗�<Z�L�}|N����)~��ק�O $��ۋ��в%I0�&�@U�q��b�awI�qS�^	"����d�Wŵ݄q�E����y���b��
�V�(��E;��yf�J5yH O�B��D�K�"��DFݡ��RlhΛ�r������'��@����1�X�cNY�&�6+=�Ky���YE�ɱwN^���#x��KL�0!"9�U��R�ۇ�ɭ
V�\AQ�J�� ����)#j�K��B��-�sH헝�^Z�����}%Y��#������M��&��% �!�2��J٩�'V���#QSLn$�#��;>"n��u�ڥ�Qq�M����b��*�Pvj�89�`�L��|~k�/D�7������־p��e�o:�y�bڢ�o�k��c󦟷.,�\���I��_NM</�yn�q.ϳ���󛷧>���cn�O�7��h�T713�b���~�=��0ü��v�����{9��t{Z�Q���>�����w����Ɍ��d�/�Nf��]'s��3��h�����@��N����oڦ����ئ�r[��M����vG�^��8{���G=~�{�q�t��{?�k�=�f�����W^�Oq������������J�,Ό*�^=0�+�:R{��:|v�����شe{[�&"�y&���>��Y���8�v>����?�����c�������ŏ����=?��x�3��_�ʔ7��_�>ʹ2z�w�G���H�����?�I���#�O6~�M���~/�M�^Fp�]�׿ ����Ǚ�ϼ��3�y����_�������1bi (�Ӹ���\TZ��F�*�5����ekE�(�M䯾x����f�X�ɩkّ����^�}�S�����!������������r@� �Ǿ}��k�M�W�m�-?(ҽq �ddFt�����co>�DI��7(�d�>��Ԁ6��ԩϣ]^��;u�F��$^�/e���zeK�@=���ݸQz�W�K_�W�����;=~ȟ���Og�������|:v��2k�2�b����si(D!� ��� �N (W�@"2�t  ��iv:��v�!hmێe'Izd%�g�Hr�N8C�j�E~�W�L���D\h�Cn綔
m@�\��,rI<QJ����,~·�l��e���~��Z�#u=	����fH_[�2]�ň-��Ϸ�eϟ����.z}� �>[7уm��^�����?�d{Sc�bu���~����������u��I�y��P�c��V�ݨ2�Xr��a=��o#�ڎ��G�ј=n��#�����0�D���{9<�s5�E�}�Xe�aQ٦�QR�ݻ�~�n��X����+�GEw&��V�u�.I�K�MSpˋ��s�jRܸ���H�����R�6����Q!MÜ�_��r�lt��о+��R���,�~�y��e��pk��4�g�]�߅�ݫx�/�;���B�Mn�tq)�jv�\e#��{?�k�4��,��j�M�����3��3�ͭ0�_�W3��܈�SA[�_Ц���~9�q���p	$=ߛA���L%��o�XY
�(�]1�}9gq�>Us�f>��3�r+���mJd&L����ԫ{
\T�ND�P,\�x���P_�}7FʚK�*TFc��C�X����IJ˸-Z��-�#�V"�ŷ8b;�ciLQ�+b���y��̛��B}��̣���5~bM"�_B�'����q�������3i�ןH�ǃ����2x$S�� 9)��(9�p�r�UYDޟ����D�) ��N&]H:�C�R,��qk9�I��^�ǟ(�&h�/�'Y�;V����Ug�|"�i%�������ބ��|�� �
  %�Wӫ�r.�e�\If��9��L�[��K){��^T{�_k�ZF���Ƞ��y�ݕ�d+Ž��3�YH�<���N ��Q�F!ڤ��Yu��7�*�X/�k������D� z��?t���C����Q�����b�Mf{�>FB!ݛ����fd���#�J��O�0�ߛ��¼R��������w�j�H�4���������H�1=e%$S�ذh�0i2!/Y�&w���>��;���t�1)�����
m�d<4	�!$j<�j�y�hh�13�ߗ<(��'P}�1�c����z��+�^�n��>�U&V���]y�H&�7(p��\\B
OF�ɋ����Щ)���\II��Y�6g2}M2!�Ʉ��J	���~-i�I.gE�x�7�3?!ns�K�d��d"���� ON ���7��+in$p-)�LW0R�f�?��k�	�8Dx 1�I�l�#F �R�����}"��Y�u�v�G'`�������jmh)�T#_�������0n��d�����ur�_6�v�~dI�L���f���]�L�{Wʻk��fA�O�P%��4���ٍ� �}빇�.\沘Xi7�g�b9����3�]�ڛlw�2�.��1��'�~|h��ku�������^�\(�7Q𡛬ě��w��u�?t{���H��>������C+]X���/�G J�$]Sa~�P����4������ko�N9ش��n�?P��M�yhOEY���c���9����ST}�7}�^���5�i�.vK���l {L�(Rb��"5f�&�c��V�M<�{�����#5b���ֱ�B�n�칀g��g��~�F�o"��='� ���FQ�A�ưn������C���+����f|�;�`u��RѸ_��DEsl#e!B��!a�Q�qs����A �@�m5^�����S�S~uةk5`�s.Vvۘ��W�6R�D���w3���<�,���[5���i�����X���MR��+�=-��l�����R�BJ�1�1u Q	'�,"����{9�zɭ�֮�,�hS�?K�ה8>l�8�L1ʀ��9J,�$���2���Oܔ2���}����9+ƯH&t�h3ώ�($A�ɹ��}져I�젬�~'y��q7�3��6����� ��+x�.��V���B!��.�k,�g�6�������ש���aa��?zuc�Ύ��VMO�Vx�ߴr�)h���1�b��YX���44c��6��q��1V{i<�:����YR��D����5�M�mx�
k�y��>[5<��}ذ�)��[�2Q=ss�||��vlL�H28���}ϲ�%1���P�T�{$#����drr��qDݪ�c_d{蕩�oB?3-X��8���dd�>����94�U�Rt���F.W� ���g*}U*���L���q�zg�2�ߍ�_��ª3�d� ����U�D� e �\S��Q�h�ֹkTho7�hyY�ОRꠢ�e�=�髒I�:��|�5N��ZyZ�m�q$��vԀ�3�+	��d��d�C�_9�[MdY>�1j {��DS(K���P����̦+���ti�1�GPx��<����%Q�
V���y�X��F�盂z�[4!�Sw�h�v�2�5̏�=c-w�u��vJ�ZEz�dg���~`�B�z�҆�^I>�"����d�������,�W�k�̨�C��5;'t峰}UaC�h�X�"&��.'��}ݴ�ٷ�)�vA�����4dS�ЙL_�L�l/�[��,��))�в�
�:4%?/����55��֙L_�L�7 �<@L�OG�A S�1���šǾ�I ڋ�����$�0,��Ȕ��E��4H��Hꍪ��^6k3��>+�oF&,LN� ���X�}e�0رL!�r�/�1?�髒I�GyƏD��'��yjﻶ��}����$�M��v�Ď��&˛��.E]YƼ�dҎ�����9B`m\��ݷx�>��Li^��v�@U��h��$:�m0Iɦl����{ywcz~֮ą��{�;K�Dg��=��I���n\Vw�څ��7���U$��_�,F�]���:��yr������?h��Pz%�����sV^5��B��J�;��;�q��m�-�zCX�w�Q}��&7M�axo8yZ�XΌ�j)4[#���p6Uܚ��
f���u~j���T�
/P��B=L�qZc�I�4cr���Ț�/|슿$�wM2����ěh��eG7�d@w��;z���ٿ/AT�`��=]��	�Q�`7��L����A��D6�ֳ��m���0��f�ԗ���ˤ�\�s�����_z�վPj��E-N��z>�Lxiv��G�Tk=��U�01 r�$��@�a�I:
��&�Zdw�1Z^o���o2���N�Z���py�m�;�u���"�?����bpi `YO:{�>3�H$���@2J�xkva��0`�J��hg|б�nsM�	f(D����bt���'�e��O�Y8u��!�� Y:�I �qP#)�2S4;�,�d���6�6%��
U4CZ?FZ�<��ՂI� f㧛N�n�u+H��F�P__z�_�������f�W�h��il��Ze�ղQ�c�����\��X�/������ㅟ����靁���3
v�m,�r�B ��W�CZ��-�3������C����%�x���e⥍�y|�A�'�2�� -�d�zd��ң0IT$�ɂ������eC'      �   �   x�]�A
�0EדS�lD�.
.+t�&���$�4Joou���o������E�a�'
E����� G�����P�qmӺ�98�^�*d�J�y��8Z쓏��bȉ���c��s�����%�sX�o�Bי�5Ƽ '�;�      �      x��}m�۶��g�_���ڛT�Y��|�Oo<Δg��[u�Nq$ڣ�F���8��c����� 	� zQ	9[uo|,S|�I����i(͂��Ϳ�w�������n��ơ7�������O�ğ��w�EE�s\n�*�7;��)��u5�xA������ş�H�P����O���c������"-\�������z�bvqM�c�����-\j�\p�L��e�'���i��X�$����z8ݓ�O}��+1L��D����E��ǣ�p�>�����i����G���~vy����?�?���,~f�'·�Y�������?����#K\�ք�X��,A)8GR�D�Sr"�'7���\/�����\�Q~�^��3�{+���+���|Y���uyx���+O�m�C/�����t�·�[W��޶ ��ͫ� ��m� >��[W��޸���ڱ��� �Y�0 	x��?�H�{A6p���D>kv0 <�l�� �H�3g`�#�!� 	y��b lsޯ�nM�q[���,��׫�������_�Ͷڕ������#�g�f�.��rGl�n���r�&_�7���D���:T���r��7��۾:��2?�M����|�ʵW�����{�6;�k��5[�0�r�k��d
�f׌i��
|�+��TSp-0�fKצ�Zhq͔
N����-͜�k�%�X3�	8�[��u㑕&�X`�C�{
Z�[J?�lوe�0�,وq+2�Bs6���L�'Kb�BM�� 6����|K,�ٚ���h���9gY��L7 G���!�B�6���ԨȨ����Ň�=�?����EdX������f�T�Ƚ�������|���.������ݻ�����>�O?z���a�}��K�d>t�Fi0��cU���j�׎��,�W��Q߆��C�8J������6�;�4Z�O�Qy�c���7�����q~82�4�E��[�=�2�?�O�$��K2���zI���=�QE���_�P^ё���y�yb��T�)>l2������[=dˇ}��Wt�u���"�{�f��C�t^�����C�t^$��a>k�?�Q�Es�?�a3���Y�����H{�|�A�?LaRD3�^�����&�@T/�0�=�8��}��p����n�t�H�|WZ ���7߅��>�y�(o����?��Z�6ߕV��þ��wC�0�,{[��w!��?���\�B�y5��aؼ������a�z*�F�a�g��x���� #6f�]����S��þ޲�q��Gr'���v��=o���������u^M��9�����@75ۃp��ڤdv	��-��DIH��lc*(� ��ܯ�պr7��;�a}���r��y�~%7ر �R$�_�����'��;T_�f�E���<͇��=�B��7{D�����PR6�Ôoz؝a�����r)���f�&���#M��8�fp����g��sV��:�Q�ݍ(�2:l��lD�������F�~������S6��D��N;�?�Eaȿxqu	c14�E����?W�w�9�ً�ܔ��%g�mT�/_�z�]�+�ED�L��L����ӑV;إ&����P�2@I�ܫ,_,������9�a�{dt%��ѹ��,e�,
���0�W�xE,C}��	ڽ��x9$�A������=�cx�/4�u���K�S��f�T��ŭ8��_:���zR��'5�{�*6������eS�ӡHFt�[��%�+.���ruDb(��[$���$<!�*�oW�N����(��}j'��&\�<����{?Ȕ-0A�����֤{��t���O�4/���s�	I��H��}�x<=J�!�h8yy��gҠ��:D]�[u���<)�r�)�!d���|�n+���l��.�&ߑ!���J��"��i�B�ɈY!e$4T�(u�S��%%��2���Ǐ�?�IB��}���%����|iH��/)�_HI^�b�٠���S�oAnX4��-��e�j���/����]�9��:=¤�2&�,�ʼ�z�������������݊��L��V�ӧ{$m�hl�w��l]����P^�@���&�z�KJ���A��@�X����Y�E=�I(�������c���k���t��?�jW�8��F��+bi[u�Un�`(mk��	rY=�&����:=r��B���<=^r��}x��oڗ�5��y��i�����o� �&`�+�˃
=J�	 ��Ш!�-����o�h��2���:Gm��dV���e�<a3����ݽ���q����u�?��e���	D�!N�*�0ᰂ�ɏ0fa&P���0�S��<.D6��Wl�U��I%^�b��Ӈa*�O�3��,�gR2 �=X���afb�9d+m�9�JsRxa��=���lg�w�X�!��m��P���X���Z�Q�����i.��V��`[�ӟ!쐻#%RO����Xf�f���c�B��F�G�h_ڍ	o۸�Ea;�����NÓFo����jV�x��"f�[�kn4X!$�{q�b�}��#�
��X���G�RѨ;z#�荆��� �Oֶh��rm|��#Jh���В$�]����C��Dɗ/�MrJ���w��Y����i($Y�&)4��OD��ݺBF��0�J���2���>�����`i�U��u�\�Z���`�e\��S	��ih���b��Ifj���.�\s@ A'��E��!�[i���vA�WD0�]"�܊��!�	��`NS`eh�u�-��+A'cSmh�TXY�'J&���V����#)��hX~�P)j'���Ea�2��⃈`�'� �`H�60��)؂�7����`� ro)�Z�t�9R��6p
�\x+[�� W)�Z$�.0��`k�]�������vA �V��͋B�㎈`�N.�C�津��P+LDsA���e�\�q@��B(�i��𺈀`��� ���f��!��\!qA�j�4�#Ü���4��"iN[Ĉ.�i"�iK���qҜ�s:r��y]�̕\���Ds����Ei"���vA����d������r���9�t�4�6�ciNǆ9;�i���Ҝ�s:v���ӱ4�cÜ���t2tiNǆ9;�i���Ҝ�s:v����Hs:6���eN ��9�t�2�%ҜNs:q���JiN'�9����tX�4�ÜN\�t��D�ӉaN'.s����D�ӉaN'.s��ٜN�9��t�2�8�)��tb�Ӊ˜.��"��tb�Ӊ˜.@�Hs:1���iN��?��tb�ӉӜ�>�T�өaN�Nst��4�SÜN��4�SSiN��9�:�iP@�ҜNs:u��� �Js:5���iNC�X*���0�S�9d�]ǿj�s�q"2�U�����;a��*;r��qs��ˍC���_5o]n �\�D=%�rcv�r�M]˔�M#j�/N/�v�qm+�����' ��_5H�\n| 8~x�������o;���1�Zo'~Gb=�Q�z;�<�#�����ҿ���nS�Xo'�Gb=�7�v���#���Y�z;�?�떙��v��(�|�C��@�}ɸa�y2.<I��ru��$�B�Q<�"���X��,Fb=��up��z ���>"��@xw�}Dx2�At�}D;1���v]�(�� �m&GoD�q������� ��Q<ɂw�us�Y��z�r��͌�zX9��>����  ����g$փ����#Z��X_<ٱޮS�� ����j���Fb=���>�����!�����X���Z�h�Fb=[k��Z���Fb}}~M�z�Vn$փ0���":��X���Z�h�Fb}�aٱޮ�� V뮵�6q�CwP�]k��H��lw�E4�#�D�ݵ�k��z�v�ZD:�AL�]k��H��rw�E4�#��ݵ�ǎ�zcv�ZD{;�A��]k]�H�iw�E4������Z��Gb=ڻk-�u�� �﮵��z$փ���"�X"��Z��Gb=4t�ZD    [>�A��]k��(���gf�M/:m��0"��!��@��]�9�(\}�Iw�G��#�t��ei#���/�t�y�Ea$�C�Kw�G�Fb=��t�y��b$�CoNw�G�6Fb=��t�y�%d$�COQw�G�MFb=�6t�y��e$ֳ�6���H��H�gkm�]k���X��ڴ��"�=�����Z����z�=뮵H[�H��~��"K��H���^��"K;�H���>��"K��H�N���"K�H�N���fB�[�Fbtִ�����Fbp���5���7��������v7
���ۆ��$KO�X����@#��g[��(Tl�������[�M|�zjb�{K޹l��/�{�ݹl�NQE8�4������[��c粥��
�{֙l�c%x�T��`o�:�-�'��:�9�\�@���V�s�}J�C��etA(�iC:�-�Ӡ�:���\����J�'Җs.[�SO�uH�ʹl��;%�!M'g�~� Tb�Br.[��Sb�r.[@��:���\��?�*�bg9�e�ЕX��^��Д+�i�8�-Ѝ��:�-�\�@o��c"M�:�����,���{R�.Ҁp&[�܏H��H;��l��w��s��g%�"R�s�f%�"��s��d%�"2�s��b%�"��s��9J�E$���l�����et�(q�����Q�."F?�-pjD��]DZ~.[@3��]D(~.[@��]D�}.[@Ϫ�]D�}.[@���]D�}.[@k��]D`}.[�KC���\�\�@υw��l�
%�"R�s��J�E��g���%�"2�s�"F%�"��s��D%�":�s�C%�"��s�rA%�"�s��?%�"��s��}%�"��s�"x%�"j�s��v%�"��s�u%�"J�3�ܩw��lA�w�l�cו��h2�eЮ�]Day.[X�M����%�e���]D�x.[�V�� ,Z�s����CaQ&�˄��2���\&�*�AXT�g2!�[�K��\&�h�!�}�[�E�>�\&D���AX�v�2!n�q�"�;�	 m����)��e�����״r�;n��*>�'���������~ ����_����T����%�kp@t(�f�M�5�E�kv��T\MY,�f��M�5��%�kv�D\��T~�z��,���b�Lvͮ���k�=�e���ͩ�R�Bvͮ��k��%�q�T\񡜍 Zթ�ZF9A��Sq�r��DI;�@�)g#�0w*���T�F��D\���@�F��T\9��� G�O�5���D`=נ�@�F��T\=��� �喝�`9A��Sq��r6��ӧ����lѺO�5�B��"���k ���D�?����P�Fa�T\��9A��������v0נH�F�.���*w9A�"�����l鱘�k�����ec*���_�F����r6�4�L�5h8���?e"������ �.Sq���l鞙�k��&g#H3�T\�&99Az{���~���*4נ�D�F�Σ���)r6�42M�5ht���/j*�Aߌ�� mVSq�p�l�ښ�kpzH,g#H�T\��L9Azʦ��z��Ң6נuT�F�����Qr6�4�M�5h����o*�A���� �}Sqڿ�l���k�M&g#H��T\��49Az'�������9נeY�F�N˩��r6�4nN�5h����t*�A���� m�Sq��l�R��k�C0r6�4�N�5��9Azh������� -�Sq~_F�F�߉��mG05��0<������l�?��GaۯLM��3Oţ�m�&[����Q�vS�an���GIӟM-6�nOś���fQ��
>���u��l�,��GyۉNM�4�O�#hƅ���_��}���8ʌw�����a���U��c�u|hh6�Uh{k�0��������a��6�w<����a��h�L���.G/�*���xh8�P�����@C���@#���@C3�͐��A�ူ@�fHk�0���F3��thhVS��:44���i�Z��h��V��j4CZ����m5�!���@Ck�͐��a���H�fHk�0���F3��n��u�h���'jHA������5� �W�@C��R���a���S)H��0������hh�TC
��34t�!���jHA�g����"5� �-�@�"^M����a�A��F3�?dhP��������h��W�aj4C�����-5�!�	�@C�͐��a�Aq�F3D�?4(��h������Ub5�!��a�AQ�F3D�>4(^�h��ˇ�E����0�п�F3D�=4�����O�j4C���@C����0РXT���j4C��C@�p6C�F3D_;4(��h��_��Ŝ�}�0РhS����j4C���@�>]�f��rhЏ���G�n5�!��a�A�F3D_84(��h�������T�f�>oh�i5�!��a��8�h��ۆ���P��?:n�_pC�>lĤ�g�-��a�V>7�諆A�Zy�Т1o�G|��I� �B�g����|����gĠ���-��a�V�7��c�AEC�������ۋ�[x,����*�js��ﲜ��ݮJrw(BʬVq��B�B��)�P�P�U(��
	�
eV��C��'�*�Ym���L�2�K���-��U(���
�Q�
eV��C���W�,jw(P��¢q���-,jw(P��¢�p��-,jw(`��haQw�C�^I�5�;��haQo8C�tj���5ܡ@�F�:�
�j���1ܡ@�F���
�5ZX��P@����r0�;��j��9ܡ��W��E��z 5ZX��P��Q��E��Z�P�!�;�����ܡ�|W��E��d�:�,w( ��ye��C���+���
�su^Y$�P@����"p���:�,� w(�����E�Z�X����
�nu
[(~w( ��U�B�C��F���-,��;��j��P��P@N���BɻC�F�R5ZX(ww(�Ψ��B�;C��8Q���Rw�2Y�
�
�c5ZX(sw( ��ha��ݡ�V���w�2X�
�
�_5ZX(ow( {�ha��ݡ@��F���5ZX(lg(�	�j��P��P@֪��BQ�C9�F%�d�-,�;��-,��;&�F���c���@)�#d��70P��90����;Bp{E�@%���޸�vG��~_G��=~�����uG��Omo` \���l"��%�v8�J.��J�@Q^�rS�Z`<C%W{� ��0(����X�AI՞0�r&*J����3UaP2�LԖ�aP"�'��l�0(��Fa59�j��FS�78���Lu��cO`2�y�Ӌ=a��T4����3WaP�'����ɷ�0�E�'����t3T��t�	?اh�����L��x�	��� '��8���Pu���WO�B�u '�z� ��N���	��:mp��'0�����0�f�ˍ����uv�\Z?�эH��8���Nuz�ZO�:���g=a��T�'Ν���S��8o��Mu��9��0�V��'�z� S�NO���	,�:=q�'0��ĉ�~0����鉓V=a��T�'NX��S��8Y��Kuz�DUO�.�鉓T=a��Pi���	,�pr�'0j����0�>�Q '�z� �F���j�D�8��I5
�DTO�&�(��P=a��T� N@��NR�8��5
��SO�� 5
�SO8�_�8��L�(��M=a��T�8��T��p��'L �G��v����C�;"_��K=�I����X�y�Xbt��R>=������y�Tbrȗ�TOϻg�C�l�yz�h�&�\��⹦0db.��r=���s�:�q`D6!T�P��	��-�S����p����>nhp�t����tZ�*���혫hh�������rBnh@?���BsCB    �8�↦�R�h(�↦tS�hh7�Z�4T�h(�ㆦ�T�h(���:&q���u�۝�ЀPP� ��qC^A�o8��-V���74���s&nh�h�� ��'���+h8Q�֜����D�Z}�����)nh���
J���Շ�*h(�������$�Z}����r-nh��
J�����*h(��V�Q*��Knh���
J�8�5'�*h(��V>����Z}ި��r@nh��
J������rC�U�Pb��>;TAC�!7���P�����Be4�-rC�U�P��-n�U�P���>�SAC)$7���Oe����>4�PrC�D�%8��V㩠���Z}r����Lnh�a�
J6����s�h8��Vɩ��ԓZs
���2Pnh���
JD���gm*h(�V������Z,�O�;��H�5FR���u�qUn ���D�a�r�En���\�?u�XN �/�T���$L��~���/ᴚ�)st�yz:��sx�P��ZN�@�DZ@��r6&�b� 2�c���|����5 99�h���� ��u�hS� 0A�Y��'9��(������A;��	(!��@6'@hb�N�ds�v�\��lN�,��y�RmN�2=$�� 0D�A���8I�4(/�<�vРԔ ��i�N� �85�o��r�H�C�=EN��iS��r�H;Q��	�#�j��UN�@i'>�W9���(e��v⣬� �H�i��;N�@$i�(��ql���(��t�v�,� 0J�y�=N�@*i�!��8����(��Ԓv��� �K�%}� �(�]�Q��	8&m�A�'@����e\ A��h#J 9٤�4(�|�6Ҡ4� PN�H�2AN��:i#J9�4(�ܓ6Ҡ�� ��h#�
9��4(1�$�6Ҡܐ �vSm�A�!'@����e�� ���F�$r�D����'rE����*r�ID����-r�IE*����0r���.�v<�z��pDZ�����r�(�w��1���4w��	��V�	'9��V&�	h�:T��ʈ�`���H�`�e6�ϲ� �mH.����*�bc�� �2o%`c�� ��V�w�Qzg l`��~��� �@4�]l�0 8����q�c�Ii-6ڴ3 6��t��3�N��r��.@c��ܖN��Fk�`˿/#`c�����#��HE����J�M+���I�N����KUO+��]HP����������
�X�t �@*�
�Xu �P��
�X1u �H*���h]u �X��
�X�u �D*�
�X�u �T��
�X�u �L*�
�Xv �\��
�X9v �B*�
�Xe�tlPb'ݸ�i��"����k��z����n����l��Vq���*���t�N������v�N�ڭ���y�Τ2���U|�Υ����Oގ�4U�����e�Ss��8���H7��-��ا�O4��4~-=蟏U����~�ӡ�q�M%LD��f}P��%�`��>(P|�5(�^�
�
vR�X�ԉ(XU�
�3
&@���\����~��Р`��>(�T�PЊg(�i�>z`S�%��T����������j\3_�jp��k��L�"��E���Dᚑ���FP�kF2Z1��o�����4ߚ������@�Y3_�:wE�-����>( ��d�C}Pd���������m�n�A���"
V��"��#�`��>(��>"
&��5kM�A��}P�:��(%��К���{�p��f$�e�>(P[��1����Ț��������Z3_�"}�Pk�Z��ܖ&�@�}P�ګY_�{��j�>ZL�\��G��}P�V���h��
W@k�>Z
��W��G��}P�Ҫ��hy�
pE������ +���hɺ
�?������@ET3��2t�}j�>Zp�UN��GK�}P@����h�
�$k�>Z.�Bd��G�}PBQ�˿h�����s���s��ǂ6��,^�s�d���_������B6���r�����[������_��^zw�=W�Պp��˧jWz�7;o_~���xO�����bu�^x��|���oQ�9���L �)z��C�NmP�/�]} �1/a=w�޻��ڬ�͊�/��������Zm��E̜�n�L��>W����4yj���ۓ'x�{���o�� �߳o�ϖ;oΡ��72�F��΍O��'}�tά���s��V��CȽ���^�ߓG�,W�i�Y��'��{o����jgw՞\�_>�*�Bv�񕼆��r8�*��ג���s�%W02�"�(����*�^Ŧ���
'�U��J�WA����q$�כ#�O���U�����y�-�G_*:d���̿#����@o�\���i�&�=Q{6�r�ksܭ+2��|������lt46�͊|B�B���+w_*2�}�k�딽K���k�:�^g�|ˢ[&D��`A���؈��=�w��H*�w����w'	�ey ���wǹ4��t��Dc�q�m7_����eI'�f[��åO�� (< �җ6/�{9�F��r��7��du��h*�#��S��Q�9�S�ϖ�X����o,>��@��������5]ߚ��7��x��k�g�Mg�v����E��S�{෩=`τ/&{�q󵹢 r�G�VdZ,�S�tN�̈�#y�&8]����������K�|ri���C�V����tE�+�˗�U������z�[>W;����o�6�!�d�Y�s�Z,���V����>�$��K �Kfp1���<�	 ��.�Sv�':$:��L�E��,�	s���],x�@��[���ٔ]��L��@�8��-c��j�Z���D�va~S
���z^��
�f����+5m���~�Ұ-����o������놐�k,�R ��n-���=���/���vk@w�aV��H�|rY�A������n9$F���k��6{�#<��튮Y;�Q�`q�`��igJ�p�����X�V�͖<H���r7?��D���&�(Y�w�'���rCv��H�(icJ�Z�YΤd��𼘼����o�M�<?
}��[�'�,OKBX�BM����w�+Hf���qƦE5'S�&�b1���MP[��#qf_K��*�-�hV\����7�p�9<2'��<&�]T� ��g#alZ���_^��mH��z�d��=����,z#ZϠ�rEL���f�����L!LLY��{����!���f�#��������k�C�z<<z��/�ت��>�0�l��ۺ|"���s�u��v��ט�0Ejz��w�q?b�%�ɟ�}����Y�W�JK��]ǧ��|����J�h���ɤo?z^�ZF��fɧ+�z\�W����/�re�ϗ��%��&*���+���d�qoW}9���j/mnybA�<��"�����n�����^-��W�xzx\�-�?�y�"�(`ֆ#���(6e2��h$���A�P٘��H��q8JM3�Y���Z��̴3kӑX�#}�bm��g��l�|e�CӮ�����=M8h<l������]���Jh�5#�L87��xVE��nL�n�H�%f����[,�/�͞�o���6G����[ �r|�wb����h��C�����&��1��Gqb���&G�1�/J��v����]C�o�i�1���d�ږ���j�`z���y�z���i�̃j��ެ6_h���/~�[q:�����wտ�����ϛy����X�by�L��\G���w���ҟP��2�����Ӏ/}�1��^ܾ��S���왰��@��;�P8S�_Ǣ�y�Q�����F��V�ɇoޖ>��O�_}�L\"�|��W�87<o/>2�#�g7�їt۶�ea�Ί���>t��w,ǣ�u���}Ǟ��tW�C�Z�r4y#�pa�������on��E��h��+e�|͌bބ񆯤�oڅ0o��x�W�$0�&�7�4�	�J� Q�	�̛d�dx c  SG6]]��DWN?�qM"7HKs�{$����������,$aY�����*ʀ�kM	6��Ku@�Q?�}�-�R�X~&_��S����Pbģ����
v����������V�⶷�w�;�n�C��$�q���G<gx�$&&�9M���$�q*Sg�i8Ó�$3%h̙d���$�M9����|��9|�V���{�!��oNn��Y�چ%q��y�jǴ%q����G��<��l�}o��c�
��0�G��i��f��T��t���/l�G��������Q㷫��r%�n��EhQ�S5#ߤB�ئ����I*5��\%�M���W�k|W<�IS��_��\��P[�LU�?z���\%���q�ǯ��ޤ���wL�E�󎔒W�]��f�M�bI�Y>i}�+��yN����7�ݜ����%�fa�Q�x�,�h��i�S�41����iL��v�ā;P��S���eW) �X5S&�6�z�/����#�Z��43%Wwn�>�cB���۷�T�q�t�w�̓�,4Un�n�h�U�G�hė�<4e����XY��f2iN!}��������1�{��|��}�O���ȋ�^1_d��f�ͯ��Ϛm�eQ�m/��F�(.��7MЩCF[U[WՂ�%b�z�1����Q���C)�h�F�sU�b6� �!#�d6���$���G���2���~�ʠ6�1_��Ĥ���L�B5���>���T�{�|�|eS=����﫧�շ�2�M�c���I@�	�*kx��3C@���*kx��s���TІ�fd���~H�`R�<�慩JA���`��Z�&F�bG����0f�;>6�EhbD)vrl��Ȕ�R��<�<���C�bgg�Nx4,�	��σ�c_����]��G���hl���[���%~ǲ�,�=%<j�i$����u��	����M�W�uʽL�ث�:�^��^��;&��?Y���߼�͟�w�?��%�[nY�{w�nI�A��{���$I�9��~OʨEA95L�V������7�}��j�.<��rM�}��tv�|�Q6�7\�eo��E����Z�n��(�2t�~�7o��v��I��*�|�);#��o�|��W��RKt�BR�%�k�q�>R���/�d�y�9���݇4)���/�}��	�[d.�<���4�=s��)�1̓r��R����9�S�Ĝ
�S��)�ۓO��'M#���XL�Ř�X��BІ�O�G�2B��n�>N��8My��{M̈́��;{Ӕ����W�j�|�pko��'0�=���5���)O`��WG�3_�W�,�g�VX�l�Z�[���w�j����t�/�@j������y2��?/���![��e�d��[}�p��v�gm\����L�+� @h��	M`�@�.��]V�x���g+~���2ݠ��z���-�I'1�P׽_������җ�Ɨ�04Ud�ݲ�ލ��xn���+�]���7�S�Xn�7���/u/�GFi�TeE����ݏ�j��ށꞶ8�g�=� �F���$��l�'Z[�vLN穴}���q��	S�qHAhlm��xŖ�,f�yt�M�y.�~T�����Q������������I{f �4����׵�e�NO�����7�y���n�|�)��.��o��'�1Q�;M�t��s���Hm��z{{��o����
M�%Y�W���Xƞ�m��<(Bk�.V��F�nˣ#����{ ���J�)3��l�5����'�vQ�k��d�p�/���Ĝ�'�?#&�ͦ�7���-��Ɍ���{ar��p�w�[�3����-����N���OhZ�7��d��)G�45�xH���H���C K*Z���}.O�!gN����/@w�N0��䕪�)5AT����������ظ����k����q`J-������Ӓب�����?ϟx�1����> ���x���k������޸��1�e��}�,�+����iJAl��x��? *�-��-/y �����忏˅w�#�.��[�YO�w���=A���k���V��/W��~�d��s'����,@{��n����L���A,?J*H�GI1kÑX�Ӡ�xB�6d�_=��ﰖ'-�)��m3kÑX�S�
���w���~'s|��#]u=�g=�Y�t�T���>�g9��X�s@��g�g�h� 1n^	8kv��ppt~�R ��9|��I��1OAj���q�%g�\� Su����OJ��ARo>�d��ㄏJ���S4�jOf��'F��Eњj��6ó ��<���D�&�\-��,�ֹ��!͓Z����fAr!h�!���*)��j����h���}���;�3�3~VT��0���p$g>g�8� 5V�A�
NA��aQA���o�*��AZ�^��?l"՜W��e��d�C��`��Id'�S�lifq�5�ER�qJ�,���<��glُ4������t�[M�>�ܵ#!���ROj���3l��Z�$ȋ�0!����o��3NH���)�(Yd��^�܂�!��!�'%Yl<J��/�"!QƏ*
�ĔaS�O�2�O��

2�ɔח�,"$�����������%ko�b	�yV���U��z�z*�G�\v�/t8������2~�O��p�7�BڲҚ͞�@*���jYO��U,~� C�>.���.����H,��̳�
~����h|�Q���ן~���%�b~�N����1��(����a(An�]�+�+㧟�qfS=S8=S��:	r�ɹ���q��#ݠ[è��h��47V}�ٖ�4ζ�G�����{N��^��`��x$��O��c����	�?.&(�����$����q3Aa<j����?�&��v�x�w�g�Fz�W�O�	
�M�G� _�����<,���p��	���3_��]��X�h,?'�Gzh�mfm<ka%�Q���X�h,?x'俪n8
,��h9~O�9jM�WYpk"S����g9+�󄾱I���������F����������Y���A:!��k�i/�aB�d���:��?8J��&�TƝ2VN���Q?�%�}�����<���z�ur6Z��Q�����t��i΋��G�5�#0��d�?�G�>�O�*oS���r�g��j���x,���$��t\�$DJ��rz�s�r��A퇕��OX	cͩ����W�������~���J�rW~�Iϣ��d,�<~�I��������$ah̾��5d
�;P���ݛ�24J�i2��E�4?�#ͧl�g41W^��.׋�#k?����i��鿐�>�ݲ���WU�~S�
E֛�t�g��aG.m�+�oe�{m|�
����B�_��B���?���ɯ.      �      x������ � �      �      x�]�1O1�g߯�Ą�^�FT��ю,�����(ɵ��BH^l��ɩ'װ0����S���=��&��0�g�)�h��3vbi��N[�{��wPø�'7�\,�<�q�L]�h��po<5VZa�Dc?��	s�"�N��DK��m����������(�"&ʹ0d�;��l�G/��տS�"�d��C�h:5�$��N��T�+x��a݇��B��+!�Nږ������`I�a`��dl͑0�7��z���d�|�e��r(�bX�����ό�      �   �  x��U]o�0}v~����!�H�f��5��j/�&�ld��ٯ�5P�TЏ�
�||���<��ݖ�^�H0�6�d�ria����Z�UP(e�y��ˇ��{,p[�q��b��N��
V�\B��D)�=�?;!Am��O"�U��iM��*�V�k!2��ٙ[��{�Z�\�?�w�q��:�}	)���27;�� ��S���;��G�S0Hea��_UB�K^�ǀJSnL�$/������j�#R���	��v�����7)	���+�����?��G���8�~?�����"|L��t�����Xa,�4GM�)2�;��87;���"Z�=��(|O6Z?��A�gq@V�p"����V�2k������@U�}c��#Q�G�*#�<R4j���ɲ��ZoD֍����PR��b��Fؽ�����@�u����*]����&�	���w�eb��������h��H�����P]Y�2O���=j(���P��ZW���(��v��>Uq��1W��U�*z𰯍�w^�8�(�;��I|o�`(�9In��UU`��}":U���~��в��<�R8���?��9�eny���B>��op&�/Vi�*�==�MN]^��H+�]�l5uג�K���6S{��"m��E�oGF~)�[ռ;X(��n4F��&�%��[��IЫ�6^7�CW<nBb��8&�	�Agw-*t�u��H{6�L�����      �   #   x�37�4202�50�54�44��0������ @�5      �      x�35�47�4��253L�b���� +7_      �      x������ � �      �      x���r�Ȓ(���?xٱ)U��<Q���jݎH�WG8��� �c����n��̷̗�̬;P A����1kZr	�*dfe�=yΒ�ǌ�.��:�E����ժ\|)��|�V�:�̓e	�2�ٔ�z��Vw���>���^�GV�M�z<�l��=����MX�	���|U>����b�a�{�'�Z�����b<>����*8��|���&��ypu#�~p�+����'��#�����m0��W�ß�&��������_�·������\<���z6�,n͞��o�_�e|���a����&X���3���a�&
�.W8����1|���˳�&�Lp����4x{��<��^��=��h�3hx�/�k�!li:��&d�0y�$�ȐK"��x0y{tu���?�%�'��?����]���9�X*�v�~Ї� �c<pϧ��cp:����������p"�����ltxda����%�����������k��=u2����H��1y2����s��`�er^����G��`x<����]�����lx�c���p��ۋ�������p89�����Fi��n\��T�^�`3���gSF?h�jڠE�m°a뎵��H�0BM9ߑ�ן�#%��1���=�,QȀՎ�G����H �a���
�H�r�3"����\�� H��bLX�1�!'͜2���pJ���>ڂ���X�$N2')�$׬2|�xȿ����|�|��oÓ���M�A�<2{����x����w`p�a.�P�w�T�0<�oX��Z���r����MxJ�^�&Or�o:>�H=�%�i�������(N����������5����>�#�\Y����9�sf�^\]����%uvf]u�M�z|�Ou�x���5�%~�w	�EŁ�l~3��"y+,It�ǣ}�vH׬�O�D�^*��wj��������b��0���im��׻���~��$������C��=�+=n�fQ��p4�C���%���E�i����w/��~/G�O�ã�sX�|"x}7[Y�{,rN���e��r�\��"#�$Q/��*�z1�px��+�����~��f�x������?�� $�a��j�	�Z_K ������.Ỻ۬o_�zF��0ރ��o⼂�����
���+��`�&|�.6���n�����x�/@_gK���zc���%�.��|�������ֳOw�r.�-g��<G������?R���+�j [ӽ��x�d���4R�gi/b<��2z|,����j��e�Z/���g�{�g	z����]p��"H*�G�?�;��4�ɃQ��X�z�w����r&p@<~|,�gT�������7Id���|�������2�9�}��q��8���~�"�Ϫ� 2Oh��$`�F��5a�T3@A�i��J��c�}�*'K�Z�	���{�8�G�a������w����D���񱑊._�^�G�>�1�������$��&1���錮���2��/�p��K��V3@���Z�~��E��C�~s5Z!�y))��Fı�GZG-#ZN4)�h�h�N���� ����T�����X	P�r1�����z�B ��g�x@��J2Rdgn	!cU�Y(�I:����b�� Y�ftg-VkDr&Տzv	��ccg����.i��yp:�ʳ�`�_�S>NW+9���ׅf�HS����	qKWM��H��^|\��/e���f��Bʅ]�L�22v�v5&��p/�O����ts�~
����Cp�D�R�S��/��C�����M�z�`�&T����s��/pf���إ�����r��#`0V�G��c^iCݚp�Y�MD�O�ч?ja���X��Vc��8MǢ`�R���Z��X{���l��9����Љj����x�S�6�y4�>���E�_��=/��$�ޚ!�.��S��� �\��=�w�F�����V^RT^�����!{��V^\�E�%���1{G�%�{�p֟�|������ aJ�C�,�L�a%1�P�q�:���s���G��ѓ9�$e}�P<�]���`%�WpS>�'�BdY,���al�P�ނ%�1�|ࡾ�B�{�q���I�����,�����d�]�4�K���H��V��*�c{<�<�����|\���f&�����V�"�~I�7O,R�nh��W6����@���7�"����>�2p�麄q6�:���
���W��+@$�v.�BGg���t�J��?O?������#��彌��l�x�Y���dtL��Ì�8�����n�`��?�O��E��5g �"S�}Z{g���Ã�(	^Q������c 0�@�D�����0|G��>#^D��͜$+��]���F���$T��5B�>�]+��]*=w�y��ݮ��W3gZ���;�M��[�ɘ���M�k��^�}.��BF�'����/.|��c(d��ޯ�V�}З�L�F�;%p�r #v��:>l)G�V�,Nz�,�Z '`5�U����_רC���2y]�m�n�Ez���J�VnA���%J����a��O�xr�&�R�2h�K1�~������e}ں�o�)�}�;L|t(Z�[�Ӈ�������O��Q�.�����l/�}p�u��hb����T{����]k�5�䒤YU�'˚�������`�#νFL�>�k�-�J����w�I�Ҷ88�d'�YlEO���⫲�(	�w����m(�wJ�F� �f���t�ȩ���.&���.\���X�x�p+���^�xV�A>����k4J�8��{&a5��
[���n� P��lEZ�IO��8�����4��N�Y����緲	�/���DK8���E��+�~���cx��c��rLNn�v��&')73������3V��^m��}��4\���uF��.H��� ���g)E�2�	3�Cpч���$-RO}�G���`F�I�[�*D�<��*S�|��w���(J3�	����J���x4<$4���wr|X�?p�>�>��w��Ni�J��M��;B%�ѷ�5p�r�	P@�ss�Y
���> :�G�L*Y)o�o����v�*D�3�����ʜ�m�"����xШ��*��s��=Hܠ�n�ϖ�p����G�%�O��5hè1ӿ��%e"��|���$mg³H�N[�W�L��bmXH1 � �	�	ɹg����G$�2\ѷ�k���@)]~��+����WX�����ZM,�5�)(�H�b�>#�S��*b!��XS?"���rW
��۸]��Q���8h��W,z�&$%��N�-�tN�����σ���p0?Ga*ڽIh�R3��xN��:�,��4 p��I������_OI���M�EF@+�፨��`��ҽ�|�^ߐIE��������_��总{dA��|�&��v$��[��>>)@��W���]�</��%��@8?�]�+n���S�y� @W���W.6+<�de��o�g�"m��ܚ��5�"�%b���`p��p�ţZDD*�R\�A�&�#.EK��I�����x�2b(��.�;E�&��M|�X.�9�*˷HqY�K�Vy�ج���] �v5.r���G��YJ�ǣ��[�	�F%ѻ�Y�s�� V�q>�{����F��;���ҲK��A�t�m�tA��嚖3 ��±�8���Am�EjИ�6��X��=h{̖��}\O���<.��M	�8�k}��U߮�/� ~��'r]Yb�\Q��ߢd�~����8{������w��3�/pǶ�B�ll6+ � �9~?������]�Ϯ�7�3��?��m�dh	��|��*���W�[�9!<bl��#�|\����^b(���\;��I�@P��m?0rxѣ�o�����ӓ��5����
M-H<���̚h4ᕙ�%}*b�b]��    ;DA:��(�oD���$��k;^ax?�_��X	����u(�`^޿vN (�q�E��� ��
���~wL�jWQT=�ٛ$�F�!o8�9e�q�����<�}Y.ӜQP	T�P�1���r̎��}V*�,��2U�Ne�ȳ�*�H�R��GWzW��(�Z�²B��f��j�G%�Q�er���g@q9eaꑙ�Ԃ�"�J��5{<
}���-�{T"!�V���4N��]ˋJY�A�W�t.)� ݡ�=��7�
��=HQ���S��w��j�%$K(��Q�.��^=8���4z���n��,a�u,����1 �jb�V�֭�Mc�LP��k��+��� �
��A]F1�ðB9�"����)E@[3p�;����^�-z���qt3R|�g�-B������V�s �lG>����l���#R�A�Q�x�E�:p�����;
����
[DG��2�f�{�q�����r^��t73�����:�kLT���$�*��u��\�W��������jgG'��i�.j��G�*��N�tf	��uǕ�֨	��������
rq��[�������:��<�50�C���܎-�C�Y$s���W2��Y�Z�����k���x˟��N�?�mחv|�@By��t:}x�c!C0��vt�V"8��iM�T;�,~�&�Vdq,y�,�,���ds%�o"֏�>/�<��۫��{�ǁ�f�����ȑq#�.����;VJ�~'������/*�������`TW&�e
8�~k�u�Ч�
�>C'N=���]�"�0(��
݊�\%�Nn�1�yQ\��)�G�dr�l�&�zI����jO��F�:BI@0�>]mg�s��e�����`d������nVs�Z7)�7��b�=���	�t.��s��	G�v�/�WO��$�d�����A�yA8��gW�8)Hs2&�@�m��f+2�������xpWw���3Z{(�&�V�{���K�J�8�`,FS9��9��m��0��&����%$�1
�<J�V�y�@�����^�J��^ь8a��	e΋r@I�M�rfj�@~�%/9�W��&�Ė�U�2ϢO.N��PABIlG��>gq�l{�B�K��/�}�_Vb���!�O���Y8��,�/��_L�K��z�ǿ��w����h;m�J �DB5�,\�h��SF�RF�s4����줋� �2E$^�c��[�����#�2�=2}߳����,�!K*!��I���a�]�K8�ȏh	 ��8��`�h������:��0��I�r�����T�C�W��j��Uw�����?6te�RJ�W����Ǳ�{y�� ������ު~�H�h5^�o�� ˜� C4r�˵��塩�����P4�#Ov"��a�\���L�OA}	�$��~�%���u�����E�s�+�xo0��.�,O��Pt[����_�l>������΀_o˲|�*V�o�~��O(�,N�a4���?��Cr<��k������r�.\����\�=�����y�s�|C���XL���J��nP:���R(ݭ+��"-rZI�q�k��&D���͛@�f�"d�l�����Q���[ :�2��ț�S7��	�L-��ϊR�x�;!Ǵ���و1�P�"�AZ ��VU�n<7�A�EU��kMi&s�(�[���K��l�k��r}�!ȝ#aJ��rUc�֛���\���t���w���b����<����>����=6C��h{	s)�m�8�	� �2�l�d�����,E4�̸
I��P��k�vϾ��=�w�f��>H�qZ�(�����:���Yˮ��Z.njš��-a��uW�`8������|�/�C���p��P�n'���MaJ�Z򩲯�O�)a���ZqI��1:1(�@ݺ�]adY/�kG�c��U�L��;�%����2_�W.2�������T}��b�!`Q�o[��Zc��~��څ�t�7X����+�ƪ*��Xu0����ʏ�F�c��~Ci��-~�o�c��i��)� ZM�c�<P�Yե9)�b,� !4!ĭVNeey��y-c�Rn(�kA�a�
B����Q�g���T�*ʇG�}{rv��`����YŤ�D�0�)���⪜��T�*n���ɐZKL ������'3r(��b�K���b|����i_u��1��ԆZ�F�\,Q!\�q���Fih�Um�������blw�A�%�\���٠��᫔k������ 8�r��]�l��ɣN��`Bdl�/4���`�S���{Q��˜�dj��S�2)JnZ;n�ơP-��u/Ʌ?�T�pVk��&F���˙b�R�@����R!D,�(�y�)����Y�r#�֡@ؘe��'Ӑ"��7��%D�I�F.�C���Xd�I�k[���bU�u;�}7�J*Pn�33�g�N�
�V�3�n�BwV�����o�fq7��m�nX�)D�qϲ>���h���Du+�$�fMc�p�+�4X�3��OUQO:.,YsQ��o>�d�͒�����]��X|�:�/{�y�iMk�A��J��J���0^�<hR��:�����u�����v7*Yk�@� "��O��ș�*soKΟ�����}2\���;EՌ),+�����W���Mi�Xf
�"'M�T��褼g�1upЈ_QCL{{]�',x*]�����E֧UU��󫣳���ʄqq0�\�;T��ua�~��>V!7ů�{��cj�!P�p­�T֨Y��*e]JeG̩4_7�X�r�Z{r�������(%97J���š@�2��2Sp�;o���2s��]��jn��qUm[�V;{?���-��C9�4��|Q,���.@Z�c�:|��r��3b�a�5��^�:�o�a4BPT=0��\��/&RS(Y���R�t|�,�[��0��j��i���Q�a4OV��@��� ��,�b�X|\��]�ZU��4�oՇF4��챹@�z��8��Wg�9
_�f�
=��aς�+|��W����#�/��3��_0�:x�����F�~p|q�����������M��Y_v�9#��2����䨒cA'�d�iP�My�.����+�p��DM����3�K!"����P9 �|�r�r����c���6�����Q/
7=���AP�o���AcD�a͆.,v���֕9�}��!���W�2��̻x�L]�z�ȶ�p�wYc�kɿ8i��1`�%�#,e�6=_��[E-��Η�\�|�4X!�\Bc�:].A��ѣ�\#JmX�Ѽ��ޣ����,��r�~pqd�I�y��g�q5W�O:��p8���,��냄Qy��W����)��4	��n��O񈣕4ISU��C�ضJ�Y�:-�֎�U��>�>��� �թ��Od%a�-���c&����E���b12��	�h�_��<�n�σwQ��>W�|��Fy����u�Zdχ��Uا�l5&dh�.̭W�+L9�	`x���8&����v~�(a��#	-Β�E���-�&:�
��S��!ܝ��Vp5���|L�
$�T8���C唒�pp�C�À'��V<pZ�`��8�l���"��2�9��H���́�| �ko�Ȥ_#=P�����`���F.\Ù�+��|��h�=5>��:0׻��@�K�d�)�Q��F|�DP�+�<f�4$E���)g׺f���Ã];�9$@�0�I��r���Ig4(�!�eT>�����U��:a6�&눦Vt$o"VA�C�<����!�->��@~N��cey�uŧ����Jmr�s��I"9��!�/�y��� V�z{��h�ڕ��rk���'���╅#��5 �+�߲���_onW7��R��f���#�XN+��V7��7���Vi�T�(҂e��"��1 Lԍ�"�W��ethF��	�N��L9� +)���-������v���-{,51O��@S�O�����@V����Hlg���g։)�<��0�J��K�d��C��{��0{!�r:�CfC��)*    ���rUux��c���D���㟺��8�//����������^����eQ�k�żG�b|������
4`?���
4�%����Uw S@�rR�<��;{�*0�n&sJ��bGQZ��.��K �W�&r���("3ފ��ͩ�(xL�U�V���:x��yy�(�&Z�m�3DD4�	�y��v�[ڧ�?V���iUOu������A�1+"��ʯa�5�)+�6���o�v+l�"�d��f+�:0�׿���ى̪�@�͵�M{R��;�Y0H���y�������d����J��ʣ�`H{e�}Er��)k�f˷�k�>��������Q��RS��d�`�3�[Q�qƣL2DVy�*�-�0k�,�f����!� �b�[8$�M�Mk2��B�)r���j����[n�ŃUYVV^�^NXc�P�^�"I�\�?�����/8(�jV���GR�q(!;<<0@���r}��q�Q�I��ت|-3k��@>>:�}�ج7�ƛ7�Z�O.���u�z۽��3`��y�皵�~<�la`in)�%�ن4�N�/Z�I��(��dy���p%E��c��3S88=[ _�,���:P�������<q�g�~�B�tশ4k��D\�nU���䜐�Fq����wID{�D��/T�@\��`�W����z�ѽ��-���ulst�%�7���sCWqY7�k��ݴkY��0�������K���9�b�qF�_�<�BX�wt�Q�-أ(A �u�\�G�qg�S]]]\g�#��|�zp�,�[�6)'�I9��@�9��&��TO"����������طVZ\�=�b�_9xǩ|)�i0�Yܸ*�R��d���t���B�%�g�U?Բ���Bj�N�rՂ^X�(�$���Pz3�@�hEQ&ϩd3鷣���\%EA'v@���}>�r������$��#)oT��"���P4
��Q��~��!��3k�C��v�fLJ++Qb����P�&Ð,���8SY+ۢ��WE�u1��#,yD ���C�٢ME\�-�A)gB�������I7O1zޏq�D"�h���t�J�w��(L��_廋�:~�(�?�X�%C��dZ	�ɫ[�5kb^�a��,����W�֓cћ��SUN��z,!y,��4�Z�Lj��K}?�p�����b8F�-6�`�e>���,,O�������7jn���j����<�'k�9��k�b�#\_)��j�d�Xw�Oު�f����>�꓏��αs�>��l��Aϝ���op�sl]4[yUK�&�E�b��T4�a"��?zq� X�#E>`Q֮�b�~�@�]��Bɍ���j��os���ƃ��O��`w0$RsK|يq��R�����Ks�k5�f����D�=��V�n�g>xG��R*W5@����-w�_�Z��I&sn���<&�O#���t;�Z��^�k)So�lgq����`�nU�>FI�'j�=;�ͅ��6����i"�D�Gappu��N.� 8�ǀK�7F��+K�_|��&�Ԟ�	��Y�R�3Q>�N\
�	]zB��B��Ƥ�A�D� �d��wY��B�R��R�4�U/x��j+�"��Eٵ0��K�Q.�o�p\��B���b���Z{�wa��`�{B,=��n5�[+�d ��Y���ܜ�T v�vɤ��ITb��Yo�Z�P �\L�K�V��jQ�>�[��A�X;>�)�#���	��f0������+\QY�<�$��l\���*Q�J
�,���<ښ	+L�у[��RBB\T�� �ǟ���Z���K}��)��[ohǗP�f��J[�FL^{�Z���m7�Z�������\�mͣ�K���
 ��a`�f�}��hU?UTd'�ep��"�`����.�,+���Jm,d�0���Px�G�"�L�XP�h��F�+A�2�3��}F����v���)C�#Vђ�r=p٩vw�?$l��")!dK�$���c�	 �dw9!�"�q�6�;��%a �Xw�|���czu�kH���` G�sɐUZ��+5}� ��X���X�"����}2��4ԟ��T��\~>$���[۔�"*�#*wR��B��v����"�J{�6P3���Ň�w<ފ(*F�Q0�s���	]�O��N�8K�P�#�P9^�v�Y}Z������o�v��Nǋ�*ְ�qX�g�.����#6��Z�wZa�H�������x��OP�qAq�'�<���,����1zpG��gJN�21�3���ܖs��b�#:� CL�^�g�0)6�`�A���2Y�|�[��%d��XJ6�iKX��-O��I-ղq�"Gp(IP~;�R��X�$ކ��Z[CK��a6Ws��@�����V�6��|\sL�����������|dGS�<�ߗT� '�6��F�t�Wl�}������j��0�v�D��*�J�dY"Fo����h,]�T7�)��v�a�}f����3J��vWw��p�\iS4��jD�8
��!�L�A��%�W����L�#%2;��Zqp���|h���Xb�9u���D@�� :�����i�4UO����!ۨ�	W���rB%���Ev�I�i-�(�˂��vU`�ji���q���5�C�`B�"J�i�����w����������dJ��Iv7��� Xػ>!�Nc)�i}�2￳�;��asvc�"Hs�:b�3�T��.VqJ`�2nx_N��vc^B�sIm�A���t�M����j�p�����R�XRz�O*����8x?<��$X���hx�O����~��F~9
�.~9��ͮɎ��9��I�a] ��1��$P���.~�ƈ�|Rc��»hv��n,�/��d�����7Y�90)6�)hJ�mw{'Ǉ��[SٽlDWiN�l$I0[��{�9vI������Y�k�Z�V̰�>�����k+8&���
�ky�'��i"Qb +l��(d��ӓ�#i[3��ݝ�N��C����#����"�-Ы~�3ou��9\{�.�Y�-���[��}��hB��J��;�U0T��T,V#b�*�(OU�hz Hh��_qv�*i�<�YTG�[;T�۫_t]$��j\�&�!�(s��ko;�]���2\�-��g/����@�S[R���b�ʜ�`�%�D�j)n7�]�֫~�s�E�p^ӿ��EI�F �^ ���ڜ�
�B�-Q� <R=O��7@J�`M��/\����s�]���~�}�x�X�& '15��L���/.-
�Q�t!���L�=�U��������F�DJN�,ㅔ�Y\���m����*-F�q�Gϔ�9�s��$-
0&�--F����8�����`�Yu��}� �a�<�FdS���l�h��vLdWdS8SθR��=��Z��c!�q���u\~���P�τ�K�{�g�J.���8q�4D�P�e1zp7o���Ae��<���d|q��L����~�&*��7�";8��S��ML�~�G]�0���<|6[�(^��!�ߗ�MGs�y�1���`�4��(�d���	 pB���͢�%no���dU�lFX��QD������Fvf���N�j���B0�sU����h�E�K6��9�eC��B��Q��.7�/h��T@f2v��k7���44��h���~�D���&��L���:Q�|*�w����H��*%�kJǴ�Py|����-������x�^>e���@HAq�Y(��������H�eQ�Rė"A��m� 
�BS�_����љBL@@^�	���5��w7VȢ���d�j�Ar͠:���#��gh�PY���Ie����T@���Y��`�,V�[F�.>����u�ĸ&���fE� ����Ͻ�'U���z���W.ϙ�QV��y�#�
Z.2$kÔ������	�=9�O����$F�OPBñ�����:��j�=5=�*
e�;�D���q��QD��t�v�@�'���m���=ؖI�L��F.�w<��    �
��]x�	�4z�?V*2c�FN�,�]c���A�nlց��aoI�.� �
�.�$B�:&"7\��ݎ�P��#�* �Q�4�5�__5hb#�E�b�Ԕ�_�ahMA��N���7d�!k��,�I�A���&\��[�zzm����f6�4�sU�:2.������(��g������~�nK�"+�T!^��ty}'[M��3�޺�t��s=�����Wѭ~rD�ژ���cN@	� ʥ?��ĺ���(�Ơ��u`s���w�m��_cW,,h�j6��rRCЀ1�{,J��t✼hdk#�����[�3g�@i_�l��v���58�6�%�QY*�a!��:��%Η�Ś�	�l���6	���jY��~��6���>`VQ��Ŭ2���B-�e��X������
��Q=B���l�8]_ߩ4֙��{y�¤nfq��lM�E�=��V�N�,;�'�B~"��c��Q�>�Y,"��m?��-�Ёq�4��҄/:��𧋖ɜ���.z������k���ad��b�E;J��Q�rQJ�#ZĘR���f�2�SLh>�aȸt3����W�k,���;���Pl��D)V��W׫�`-�����(2�s^8:���T�H+�}��8o�BsȢ���Q��i[NW~�����_+��t���'P;�wN޹Cl|8�_���z��t�c��T>'��>l �H��o9֕���V���kD��!0��U8�d�"+m�G.�R��ˢ���l���xxEM�c?�m��Tq۶�.��ȥ�j09fWWd|;%�D	Q��E*����=پ A׆Y �����{j��FC��-�wŚ�����&2�����|/��t�vJs��
��x-qk��W�@K�T���,E�>��J�%r)UR"�Jǿ�f�6�jA�J�־$^&7�!��E>A�|[�cdTq�me��c�dl� �(O�p/h��fV2V��i�qU?R���h��>
��h�����v��3h]N�����Sn
�b�ΫH4��-��hI;�0��G7Շ=	|��'���0��\��+�����`�`إ�I���e�>�V���Ua��P�)�R9�jMx���"��Ap��\d�l;<Uh�����~�&ER񕝄����8�H� �٥3AsvTfą�Gl��#M+��,�
�	�k5U��.�d���b� e����[�$��|���q<u͐7������D���9���(�rx����Du�6l�q���g���}����A�� :1�(] �QgV���'��2@��v��b�~���/���2�NY�� I���	�e	2��
���Բ̻�[��I`hn� �&�;�v������{�mW��|`�`�n����w��V���;��$]	��#��Ι�Ղ[|�O��b�%�q���1�*�'T�-������"G�d��g۔;��{A�:��b�x���s�C�^@Na7��ҹ$��#�cSa�_/�dݬ�?��Pf[�-/|�"�Ĉ`1��e����(��v1��J��\�1IK�c$�Eg}0�_-�?�f�8�� m�XN������l����:k��	���⫏�D��k�@�6�� ��8r+b,��>+��1��Xw_"�}��@$�jK���b4����_D��_�xE	��� G�����w�S*;t�e�5�]�6��9,��w%Hz7��=�Ϟ�+2*W��5��6�K�����hQ�a�^��X�v@���,�B�,�ofb^AK��0F��C��g6�/ȘŘ&$�W�=��L�R��_�~�b�3��,���'��W�:���97�g��en�Qs^��n�Ҟ
�#��F�vt0$N$7��]�
�Am�e��;܃���r���H�t� ���B����{�����ʝ�C��ĢG�YJ{(���1��G��qh��֑wĒVr����͗A06�W��aSXw��9Z�r ���U�Ap0ן�%+馚���f�K�T�]n0��DSh)��jk����K1O-�	-u*
az�^>��0���QQ��,�¦�6}-��@(�S�� ���������(9r)NDwu �e���f2��˦�O�aP�I^�oh ���rw�3IU�/�z^�ǘ��ٕ^�\��h2%c�K��(�QSQMZ�S)�nc�B��R�8�/A��&��e1�r�St��J�
�[�C
���U/w-�jAV���ȻPۿ�M�}9lv
�M�nK�@�����{T�\�M���(+�X��wQ2~���Te:o�,_iǖp'&D��c��Xa��A��`E����D�j��@E�9HjG�hBЇ�����2���o�l ���c��	�z�\�43�K8V���Jga�ϕ�خ�"�"
�r�M:Ȝ:(������z�������.;�բO�j�B���X/�� �k���K��l;9؞YF!���r�enݖ2�|p,��H�j���u�1�L�"�a�Z 7vL�8�r�;�<��&� JI��[��OTm5$/�XR�V��s��H�0�@)~f⢴Y���l�fmQ1�ߛ�
�=�]%�cc���ԅA�C��Y��$����Тt-`��R�&/+aD� ��5$��]l����,�z"\9%=9f��ʲ��j�Iq"��Z���.�]�.�Lu�E%�ܻ;*��	���-99Q�$�ME��:�X�)�Q>�a�#��Z��㝐�A��9�偺b�}3��%x�X���ng)C���I��%������w���G�Dqh��C��ҟ��0�U�z$<\ٷnf���A�BR��BHvV��&N{!3U��U�ڱZ���
2zW�ٽ*F�B�DN2܈����E*}�O )��3�/�!��ڐa[]ĕMs�zt��v0 nS	&�c�56����{Lu����)x1�hR4q��x��JsSI}�Ӗ�CK�kL�Cf��t!`u���Q?��y��I"���U����Dny[�+'�=$Cu��ɷ"�x`挨̭Z]�S�-��@(�BT��q#]2��zv�G>�}�7��g��U��dJv
,tU�߻2��bY�#�2Q����,��#_��_�#�����XW5�ֺ�8u������y�n{�^�1��Y [^=��`G�O�.(�OuT��������V����S_�
�)��SUܝ}�B�OK��*,`�cѮ I��ɫ�2�Y"�l��{͗�R�+oT�ʷ��zQ��V�����J�fs_վ��6�A�_�����
e���i��):��������qۙ�E�}[�����x���A|j"�)�3�c�dʈS�t$�P'Qpxt>	N�'���x2��wGMޞ����O���`�3xm�Wd�u廉�����dg�H:R�sk���a�JH�
��O����?m�o�Q���Ic�#�p7��.��N/g���=��\%���ڈ�go!Q�b�6�R m�c�V&;G�1n�崁/���v�oC��E'F�z��i�x'V�����oeŹuu�n��X�3&F��9���+|VY�|�"��en���ɩW�ٹ �7��J��Y�a���\��������,�>����N�]X���ɾxwg{W��KR�	���|�X�,����d=�.��.�
>�1��|YJ�Sq�WC�嵙�c���!��Q~��9�Ds�5�Ƞ�NGA�N��%	�0w��Pa@��:�Lh5YAN׋�:��'�s5a��;t��ޢI4_/L�x�rn�fជI��`��<��r��s�	��	p,�4���1����G��P���u�x�D����#���o'�%���k7+�d<8X��OP���m���-Ā��+�qX� M����|�9UM�Jgafߥ���S���ݮUͅI@6,`��U�SL�jQ'���2j�� ?1"�w��@�o_��ͅ_}"cH�T��0[=`�x{�w��f�CDu�o3.��+ӎ�-7�]Nڈ7��Bo�߆����}�j
���r�_İ��ws[-�G�K`?��"����r��X7�    Lƪ�c�+�t"�;�/M�c��zz�Y[S(4�*s��R�O�&��UM�X��a��S�9��36DL��x���z��4���q�5�����8
�#%�+�-�n@�S��Q�c�c�u�|�f1��o:���I!:�&Y%k*��S�E�����y�VJW���-�"�&��f" j7�0�Z�0z��J�62��RR@(O�8�}�ө�/\���ŭw9gdL
}N�jxz	�+��Q*�@�\��yg@�&G�lu�@ &��c97���'r��F�Nyc�D��Bd��+�R�%�T������C�@cb����z���V���vܚ�-�j�d���`\^sZ?9�O�C:6����t��V�I%�Ĕ&��]ȇW�fO� $1YS ��n��TWi��X�T��b�I���@ǉ�թ��u���^ÐL�pn��(��ee<�3��n�y�X1��;��6�w�Mv�_��#�"j�$;G��fjx�~�fe^~�g�E�}'�X�z.������M˯�D��j-��',I��������&
l��T�����b�j�z�b�`9w3Bq��G���1�<��y4&+�a�m"�h(�^�M���S��.%|�6�Q��0�ۨ^�`l�J����	���D��G��0��sY�\��x��	Xx�vJd�a�^(,�\)s�e���} ���
9qbQ��溴}0�������;<�8a*m!*wv�D�m�f�j"���|�Z
&[vb>�-�'�Cy��p(/����Ⱥ��[ӈg�v*�9��vڙK7�u����mu5R�r�L0�q��^1R�Z�?�I�Ȏ�q�:H��V})��峹_�K��dGTǎ*�He�~1.ݼ젖 ̋�.�̀��R��<�ju����|$�b::��«Eέ­�^P6�7Q3!�R��=���E�:�L[}^�r��5�q��:��xfD�T}_Zt�z��J:�@`���X!Mݽ�A�z�1'kj�-j�<�	�S�u���
w��vǧ���{O姕eWmE��艖�G9#J�V�2�
���)ۭ�ۦ�W��ێΰ���#�y��N4�>d�%�HțJwG�ɠ��
��j\�h�|{qv�cw�ĮK�$��$-�7>��_U�B�&�U����N� �TQ�߬H�8BeRwzѓ�[�ט��.cq�gD�טD�f;�JD�����H��,g��F{��'�Y�T��!�<Z=�)���os;/+��9��0ҏ�^�b�r����fvC~���C&à�R%R����Ђ��6 ��8h1lXN��l�7����q��,<�1�=3�[���ϙ��/��
=�p�����A$n	2;v�-c�sS#妼���(t�)l��W��T7Tǰi��F�Z+�*���l��.��#�Ta�����T��0K2Y�(d2�?��z�8�>Ổo~5���Ę����7� z�b��Lr�!����b��� E2���A?�f�\V�9�F��F���S�:����ʪ�y���c���R��F�8��������&�]����Ea�JF��
���prr�ߞ��vVJ�f�5�e���N��4O��r��<��|O��;��l�`�So��L�|b�y�����r�Z$ꏪ ���]	���7�ҫ�P�$l��p2���o���z���5a}��	���4[)֑�O���z&~�5���$�ˮ����\H,s<�¾���k��{���]�<����;�j��/���Fwڈ:"�L����?�����s�c�zM��^�׶�#&�d��~�Jٕ�U$�+w�6��7�\F�9�z�e��3��I�Nex��Rb�&�%�6�R�q��q��,�l"*�
�`n��5'{R� [�-�Z�@��6mI�����N`�ڼ���S��ey�18!b�c��8b�0ĺp&cBJ��L�w�H9c��Af�\����㨪��_���Z��,�>-���p\(7���H-����ѥ|��*�,U��!'��^lA��?m����yyO�[��l��ڑg�Kϛ�b��ѤPMED2���s��R< ���j�+�#v!z�1I�1,��"fF�1*Z��،��r�Ȳ97u�qQ$Q������g*t�?]�*Iy��D(����.��B��|ƅ�&�8�)�M���9���wx�s�#�<���@���ɏ<���1ZU���˙�%��=QҘ($�W@�0 ��Js��6]7��B��ʒPb�)������ٲq蕟�g��#�bi���찦nw���Ty�L&Zn<�@�Bv���bSQHs�U$Q�i�.�X�VՆ���a]�̘͌
1��ܨöZC�-��c���J"2K�	�9�RB�_�s�ba��k�AX�R"�'�A�JC�����W��|���b9
!%��w�Ԃ�b�,u�|���+R�컕��#)�,�{�R�r�A�H�����AC&��,߾���a�5n���A���ځ�L�1�zQe��~WN������{Qf����ݼ�,������5�+b֣wr�Gd��S�H�萤�������h��ChV /�l��x��V���&RNY�W�M�k�$5��25ac���������f1�\��{�SR��^|���[����������}�R�F�qD&Ƽ ]jـ����	����<���n:*:U��w�g�y��3�˒��B�:q����v��d�+x�)!�D�]�o ��Eu���x׊��Yk{�,�m�@gq��u���t$ᇹY�3��\+ݤ���A��8��q����j��g��#w5����o���ʵ%��rQ��+��E�1r�HRar��0K��Y��k��b2�I���V���Z��鐧�o��th��Oe)s��vXaI�qI��kɝD��T��FE��Z\����[��J9�U�;�n�a���G�Q/
)����"`bV�oW����.����~�;p>f�/��>��x�I
x7����JΉ��t������[�'{O��M�N�軤K�".��Bct�����c��/`*��̛��2���lq@� 4t��$8�;��q���.i���[A��l��Siښ��r�S%.V�`��yG�m�MbZO!����}�f���������=�3_�u�|�
A/�᫒�.�"sB��}�\�|���	9�#�+ldh���"
�M�y)��8��*#ۻ���N��M1�/F��l�'܆��K@��Q�o�q� � k�sV�Q�1�/�S(_|�%�R�������Ƭ.9%Z��)�;�x{�3�kٶ���<�~�;kբ���Ъ���� <q3�ޱ�e^^�~,ݔ��5�K��eY&IX=�a�ZK���'��b��r�UT	�Ms�H�8oU�Ӡe�5����� �f�$z�d�+�(�\br��(8��?M�����4O�����x|r�SpqLy>{���Q0��������l��_n�?��6'��z�����/1�T0�HJ/^��j4)'ŭ���z�c)������^�ha �NVh}�F
e*7�q#�����̭�M�B&�X��Ug)ܗ�q��Zu6�|a[��\Ĭ�#�c������M�s�]H.��uL\��@��!htp�rK>�\��5�ħ���G��;(m�p������oFL�+��jk����>؁�k�U�֧��MH :l"b&q�5E���r�(�ߨ9��Ȟ�U]*���/?�[�:��*��@s�M}D����8GY�L�wLzj:������������ϋ�	y-�H�ٻ�Ga��r�T
p�Q�$�Pw0�?u�:�?�_%&a�����,Pgdo�G����j�Xm�P5�^뾘V�ېG�|�Vv�0s��״XKz(�&�c�`��Z���*��U����Mb,ٱ�w}`������ߔ��Q���k�Fd�q��og�)�<�vZ^���v�[SW�2F;34���O]X�)&����I�-�R9�~��� ,r�V>��ee�ɱ�ֆ��&�%�X,�+�����������|<�zw�����Q�<=9?
.�]��da\>5=^w%!�a�D�    �w,�h�&r�����E ��R��0�\�%.|r
N�������0��).T�� 2�:Fh��w�$B[\8��Q �.^��e	k��5�vu'�e���X�ڥ��$����F������22�H_h9A�[�ӽѿ���~j�Q'�V3�Q�ؚPl2Y�qT�V2���.�."-(Zc��}G7M&s�"͍A��v�3�Y�,��j�rmh9�[k���v�5��ӕ��mm�9MW�m�T��&��*�g�����e;�:�.T�yBA��C������쵽��-W�k�l�������;5  ˥�=3:T� ��@sM����B����8_��'�[��[��~=P	�p�T[,5�;�3&[;�X.f���/l���OWǿ`�q�yQ!2��-W:q��1Ӿ��5�SN6�F6���I�>-D�9��eSS`7�*Q�Xj[K�~��ꔫ��p  �9�u{�������ZVn��3�J]~QQ���q�u(k�e==Y*��:�Bx՜n�a1 ���W���5��Ԅ+��>\���L�$�(��^���1|�*�PEiH��ܫ���z�Uvgq[^=�>�^�����`{|�k]=�'8.-FkU���ݱ;��񚧉�r&b��J��S3��0f��y����J�;Zm���zG@�й����!�nG�,��"1��c�.�E<����X�E�V��Օ��3�^`y����3�\?)P�����鋶���n����c���Y(qyr�@�Ps�����s�ҍ�/�芁)�> Q��"ol��b��*��OW P~�[.I@ �IG��wzg���a�.�j�5QH�������*�ګ|FU��x���F��t���+;i`Ѱr&�B��D��Q���qM�Vg�m���Pc;��Y$�D%}����l2�ty}'�tϦ��{�b�^��o.fU0:�zLZ�;z����b�lа��2���yU!i�z�2w,�<�Ob$��^�D����'�Vp�E�O�@՘��6Pi�ߩ�2OD@P�tk�E�*��{����D�3֮
��[<��qd�H��`��g{��=����o���\\:�CSB�Q3�'�ޖ�`��"��� +�u�L��qU�l�7S@¼\��e]ՙ���J<�v�R�;��b&5�j��x������JD��-NM6���7�`�u���#_/�|)_MA��~��8gp��&<n�V�d'���>��^���<�e9�qU�h��<���㶰=�=V3���jXN����'+���Q���/�gŴz�Z�`�%V�\����C��!����1#)ǫJ�J��6�����{�߮{f�*4�҈�d�Ъ�7�Bi�E��V:�����B
ᘤ�H����%��Y�eW9z��SUz�����*���<ɤ<��x�5��=��W�t���B:l3��;i�q�H�2l����"\��~�eS-�ZT��C$M�"��<"(2e[�w]��))��T9� �[u�QP�U�U��p1�֦�,]��S�տV��dsT!�Z��}�h��kKg��߼#�2��\��װ����#O��JwWj�v���q��jЋo�~�`��OwըˆFu��)OG����?.�>�@��W�&��������<'c�>�Ox� ���E����+�:PT�S6�v	�?>:���@yܐv
�����\����ח�ЊB�GwaaF���ӅhGG~�hx��s��˰��+���|]�>�����*0��|S)�n|~��#�$��މz�u
_+��4 B�'��.��� ����+�M�29*�������lK���3d���u7G�Ta���b~���i��R2�N�V��H����rN��3i!�D��xT����\�^�E�sj���J�Tb"u_BOxk�)�Y����a�A���cQU������f'�S��sI�od!y�E�-G���w蒷F��B�n����8{h5X-�?���+�R�	��kD��w'�X��S�j�*�4)��	4T�FV^��!�B�q9��@�%��'%��v�6�XV���&��D�X���+@���^uUB��!:F��B��I��̗����G6�1�ǔ�`�㯄��Ņ._A��R'L(;�"a��[*�L�F!ލ�D;���Q����\8�l�k�X�KTʘ�x*��?�BFݶ��b���dqR��K�Loԧ�?�*�t�8���-��������pV$�sLc�KԲ1�	0"9�4�{��h$ۑ.��ix�e�%)�1��r8��/`��>�8>6�F�8�d�g�*��x�r��J�/�&�!ݺ��x���E$E2�-�cߵ�c,�"�3^���u���f�T�m��q��k�6�J���^ʭ�`4����|!�* �VB��ۦ�����%�D��$���ۓKeÑK痓f��ҭ(̳�v[�Y��'ɊT�˥FǙ�:�GA�ɇ3�ZǛk�f�T�/M&S�+�Q\�k�e�?�$I	3���FP>���"&O��n�V^j⌛摜h�`�-p)��v�����Eғ6tG͡x�>�:�T���Ü����:I�lx���w�ct�2�ڇ������'�b��b$�^��]t\����٨�K@�A)6���C5���0�9��G��)�o�r���$�S�zY��L�92�5P2J�_ʻ�5f�.������r����.PY�(�X������-~��Pu��E-�Y�r�l) "�)M8�\1��#<� �P�X�C�
���m"Q��s��5M�k3�yMu9OѪv7��������b��4or�f��4b?�_j��õw�����@�4YUS��n��3�:9n�5�>�+$���֨�M�Y����
S4����7��)@�$���GDu5�V(ے9y�H��e>�+�B����g����i�B:)U]�c=��Kю��"�8c	3��t�2����� u���5��E����SpI�r�r��Ze*��}q���u���0�V
���;�*���25��Ԥ��r��S�wnn�Յqӝ�[w.���;W��ɮc�T�V�V0�4GWc�1+���o>̍yD�I��"����\�LC��ͱ�D��*��`� �����p�dp��ԯ�(So^����뉌�1�����/5�V���ܽ��W�!D����oO�0'��Se�0�ud�,ό1Ss���%/Wޭ�A��y� W��.�XyLiߡ]�!�N.�a^Q(>̝Ӊ���u���ӵ�'wj�${nΥT�ujE�>�=6�z5m��(�Һ'냍
ǔk���A4��S������b�+6�c��/ �vԅ�=�즂F�.�\R΢�zK��
���P����W-�t_n�����{��-b���b�vO�����w:���N[��8�U@���wr1��aEߨ�8�{l�����(4D����%�/݈��R���,���0TB5IP���RF��'0R#ݘ������Q�Ξ�HU<+`a�4�S�x ��z
����M�HEGS¾�9]~�?�am����4���u�4���̣�`�{�
���jB�Ź�Q������U��f�SK�[S�T��О�PJ���;���͒�mӍU>�	+c�n�x�p�T��SVH�bDE!�׹�c*�e����wa��,h_
��]m�h@e��Դ���b���d��B���G��`�Pr�Ϻ"+n��D;��*8/��������b)�3����7/1� �~\��q�>E.�N�)gr�a~��j��!�/]7��R69_�@c�`��G�ՍZ(���͊���t�$FUՉj_�ʢ-���޼��]'d=��	7sV�>��,�lr��A�Xs�Q�y�X��4�^�c��8���ŘΪ�g�;V�S�H~�7��D����"�����5�(��=4D�HHف$�����.�܄dus�D!�-OY��(NqF�����J��.��;?9��84g�K��[p)f��0XQ�@p_E����*��T1q��p�L���� 8�J#x.��y"J��f���I�ꖇ8��y	rA���Px(�ʬ=�nӒ!��U�� W�I�X7�Fy��d�˒��� �ӧS@��Y��D��,�1�1��7�>��    �Kc�7?�{�b^-[9��~��*�P���~={�/e�K!�Z��8�oU{�ɮн��oa��t����1�4D�$�Xwړ�>�vK�	�g�d/7��:o�8�_W�x�r��
�{�Y3aG}1h;)Um[r
���+�˴���t����8Ũ�2��(���t��Ɣ�I9}�&���#��f��e�B_��SZ�K�§�e��ܔ�S��
V��-P����Z��_c�^p=/��1��+d�8L,Qx�z�'F^�����®R�"��Vq�&�w�Z��a���~:���;�{�Kx0����fSV8�<Vg+�sѦ��"���ۑ�ہ��nĆ	{�	�m��(B0��.�V	�M���-���5/��^2uZ��=[����{���§���ũ���n�	ER�J�Z�i���d�BF"�[������CZ:����ܸ2��Ü�T8����9*��F�)�56��sͮ��Q�Ca3E��P�Fb��AF�m��X��%�z��/��(��ݒ���%��t�(�}ΠƱ
<���Z�#�E�s���� ��Ӌ���'���_FA�p��{��v'XH[�ܚ{��d\9p��K�����D\+f<�H�,�h��s�(F�g0oW�7(BI����8:ڒ{D	��i;m����^�A|���;d��(����b�5K����U.פ�����,���rh}�W+����eu �c����06r������Y�����@����5zL��f��t(��&SΪ&+{N�0�V^����uU���E��M+3���F�l$W�n�)��I�/�ǩ7�W�t�0u�9m����-,L�JE�icѲ�m�+��f�«@0�`�;y��*�'"[]`2�/�Y�P�%�Udeg�2c���a�������$���ب:�$������#tbʤ�A�ߩ:��Arx�7Gc	��������ޢ i��0�kv�-|�1���n�g,;�'��ƫ���2�UdYۇ��"�u{;�H4�����y!����.�ĎLi�σ-^�K�WL�j	6�e�mAF�`��K�+j��d��$���P(��":.���g�~��v5���nM�i�!�3ٸ��c��6v� �x"��avڭJ7�z�6.??%�pl'���t��_#���3�rvr��H������&m5���/���tpb)ny�>��?խ�>Y�-I.v"Hm��fK�V�Y@,����͚|
��-q�l��%ºAWo��ڈ��3�Pؓ�ھ�����8�[�	Е3�y|�<���.�Ap0].����y4��;	!�7�E1��4�5+W$tI�Ve
m���FD��_K�y#[�xv�R��{տ������#)��Hf:ԫ.�2b���ɞ�Q��iEqΊ���iR��ryD��C��T����}w�4e�������m�S�c֌A�'ؖ�x�"ۀ��?ګM���'��	ۏ���h�۾��*D�f�[��l����ع��p3';x��Xg5D�[��-T��*o6�׷^X�*�'{0o,iO�G��^C��%t*�{��,AS6�jU����-�݉���g[m�.��]��!�钐�E�
��Ig��L�I��6���-m"�1p;4�4����VL�G�TZ8�
n�{̩;�*-�R&�E�F��!�c�,� ޔ��}�jQ��0~�Hh�>��B�g��ò�;"@�����`�
iS�b�����~�&tj���ε��#^H�$��@�9��4�ʺ-�v�8=9+b+^�Q���*�8^�Y�
�w�,W�{�R'�TϹ� �`"b����tJ"�KE!��(�Js,�eY��U��~����#�rvj��	��������Z8� �v���Ǹ�H�0��`Ce����r�7�w;3b̸�ŵ ���Jr��iFQ|�V�{pw��&�%LU5L�#ToF[��
6�u�;�-|[H���NaC�nG�"�.�ź�@9���)\_���w���_SB��-���C*��L���L"��Gq-&:����k�j[��4J|�;�;\�	�~��u�!�;d/̌��Ԗ��S������`��Z�:P��t�7�Y����"��<��$�r �x�4�0�e�빀�WG��v�]*o���m5�+l5ba#jE	�{C,?�bv�%"#'yi4~8�Vz�hH��qh���*���f�.��`K>�IB�x��Kۈ�{��])ry��۫r�*�|�h�~j�D�E���|z4��9�ҹ]�j7{�5���b�N���j-��D	�$�qFɗt/1
�X�Q�Vk�IF?���������P��p�ݥ��#UG�fV���`����j"{#*@e,uQ׉���g�6�_S; �%����x3��۵����L��j�����>n�}�u�?k�hE�p��C���¦P4����dU���h�.�����v�N���5F`�	��5�mGg���+��m���|��u�\��%o���:��xYO��Ί�e \BWw5F��\�vT����A�8���[a,bZ���z� g��[��J�������e)����9�5�Tz�_��a��z#�5�-���akR�S8�6?n�T?��}K_�DE��*�g@@p��`ቃ���	��KE�T?ש{?V����.�� Xcj,
��㸣�Т�Q�O\K�I�:�+����MP���7�X����M���F�Pغ'.Gl� �su�0���������J��̱����d6����a�P5��cSKB���<z���j�]¯��������
�W�r��<�N#$�e�s�X0��-�X5~'E��b�E�9�]6�'�p	
�=���������#���w���	���E5���+WJ�3B �-X,�K���z���+i��
�m.R�B���f�"�!R4\r��R���!�C�R��0���}wGd��4n��v�����f�!�7,oh�Β�Ԟ��g����@X�,N�r�k�w��۵~��z)E�Q%X���ղ�\u*��f~T5֡s��j���M3�a�����Q�=h���U�ͼ�L��L&1y�x�B�*�ֱN�i��٭��JZ! k��,)˝�HI�Xk)k�l
�6�v!<�n9�:{-X� 8�BB��c���i�#5N��>���\vȅGMr�� ��_P����˒X�~?Y��1�y�{@��DI��+�<����D�B�Qb�L8f?�E��ɕgq�cr&�C��[��8Sc���au����1�����e�Re}�?�۹����E5!Jc�H���Z�jP��M�Y��:�l��[����VE`�M峿K����}@�h���{��(#.O�C��MU{*�����ij���F�������`|t89�8w.꣫�����bt���i9
fq޺:Y�`AO��8�����Xd�iŷ�Mb�b�]V�#1���HL���4�bc�yTzo�p4�U�4q�\K��� F��/�:;A����x�X�#�I��~����Z�&����(/��"��g��K؝0�ӯ�I��صT�6�Ȑ"2��J�n��g-�g�~M2�adRX-0y/f��VꣀC��0SP�K�į"߹t����@Ҋ���H9�v��[^�*ɹ�O\i�#S������Q��Kr)�.�A�a��[w1�� ��{��+�B��	��JYv�+�_��{��@|���ޛ��ul[����m�,���fc�>���2�CR�O� !I&�<Nf��������T~�o���#ΗܘMD�+VfR��]U����\���1�1ǬT��<(��3��MP�l���@ݢs���	��`��da����,G7����:wy�,:�MA��o1��2�����.��X��&�0ܝ�T%�Au�r­CG b�����w;�6LU���Z>��ֻ
Kp��s�l��[� q~�S5@�4�.)^$�W�1@��6�&h��ɱ�Ƿ�u��^@���$�������YGcU��9��*�Vn�:�������v�HbmG��%��LeQ���l����,��.����afB��ŮvԬB��    ����C�0w�K��+�> ��؝�Fo�K'z���&�v,iW�inMϴ���S��¯��x<�B�.R�:���&_^�,�au��v���Q��}7��5A���$a^[=�����(�������-�^���k^/������kwY�h����}��8���%V�*b�Ӊ6�j�'$���56B�ޭM� �u�t�i�l`@�yJ�֡���`9^�\$���V8�}�pf�H�!�ꔴFy �F+pds���X�u���{�:��ay_�zJ/, 3���:��2���wP��S�g�c��;=�"n��%tKs��J�Vb���.:&2Z��3��|�����Ȉ�׭�):�>�9F�{�����Qu@Ԡ��E<������3ׁ��f�Q��uUvk��2����Y�����T�Y
�P{�,`���u�F�I@O
��0��ث]j�X[�x1���fؚzcg+�L�$;ג�n��u0~��-��J��_�.m��^zx�o�2�{��st�"����k��n�la��L����gh=ƫ��
��V���QC��D9QK��]:q@�ꁚJ%L,�{v�K���w���F��o�N4L��MVn����X�u?����w��2~Ux�	�k�pX�u�k8����ͮ���l���A�ס�w�W�u�z+��LA��5-�Xo�߯ȿ��]�����e������b(���/:�N�O9<�Qb�b�c�MX�OE>b�?�y���y�gf�����u2L>�c�N6%i[j
�Ǹg�6ۢe!�@)�3^+i:d��]���=N�����p7e/�G3ֈ�g.���v�]Z���LڗZ�z��I3O�;Fg�.���Q`�����ݿ�zB1�sd��+�fYA�Bꋊ@zB+���֬R��x��[����E�V!�� ��(�^^	/N��#�ӻ��,�n��l^ �7���Q�$�|���,�`��A�Lp�P�#��v:���5�������,E����;�xyM�_�hH9{$RF!E����?����/���#i߄D$%�,3�z�X��?��B�E���Pcʡv���4��<�kx?�����L�w�l98�q+��@*nE�b���1��Җ�J�#�������MH��{R��'Q��_����!7�]�l,����}t�(���sb7��������`�*�^�b,E���
���`�!ŚƲ�1��m�%^%�<������_����_���8A��wL]bv���~�ed���M8X�|���,{�S,�������[�9s� �:l���u��E?|����H"��t�����	W3^h@&�D�gC��`\��&+�
`�����b�&eQ����q�౾���5m�˫��Ej����.�AW���Ɂ��^b�M����*\��Vt��ĬԐ��<w�wu������n3�Z
T�DxX�T���pror��� 2�=[������m(�h�K��� �a6�MvN X>�I �;�oJ'��yf�(�1�Mpn��1ʀa�����iA�
��/M��Z�6f��i=Fu�YIl9Zڸ��pouݏmC��H�Yڅ���9.���</��3_�ѷ(�����`߄!WID��&�X�\���e<���|�a�t�J�2oo~�y͇p���d+���S乭T�(�>�a�_Wiμ�I��J�X��|C��~P ��k����(�!�h�䳎�cu�+ Dx��y��2��\T�tRC/t�z|�wp��������u@xq{�u�_!^D�x]�Br�ؿ��G4�z�7���I�atp����xV��x�;�����į����z>�}�8H0Ú��� /��8��
�.`i�:u��jH$�b*VD�u�(w��N+A~
w�Η:���������K���p��@��Yr��B�G�Pu��n��!V�C��e!O��[�� zWFR#i<N蔴%h7@sT`7�ά~C�%P�[|2ت�y�q��(Sզ�*��=��瘷]La��Z)ϰp��fh��&�1w��-��Ա��hY���:5��UX�c	�'/m?���
-���9<��U�<h�ρD~ VQ���9_��~-�D䩯��v��])Y��8����<�b��:��/�N> ���n�t�`M��n7Gk�R$�� �3FV5*���$l�Α������;5���j`��<��!#EH�n]���J��<8ܐ+O�:|b��n%���g=/EYM.p�s92���E�GVFك�p��d��N{�y�_�˼``!�������p���j���T.��"M�.Nl��N�f��gpU8�h������٧�	V�G�##qPY�n:Sv����.�|�m��v�E��l�F���ߖ��:�����d$����ZEU��uzX��wkz:渶(�r賋 g�:ٵ�J�g���{��o-�)�/������-�)�^a� ���Tk�S��N
���7��)Q֝�}�)`���L���6��i#K>��㜐��$��Kǰ����&T��u�L��I�\�;�xI҉�9x����i+嶢�^��V�&�/�˖��Z�c�ڍD�2"���@V7NQ�0��c^�EJ��S��:��o���B�pZ��_��%N�i9�c�γ��}N��,�ۏ�c[�Q�g�U�;��QJk#�mU��tF�aO�kV9����(�e���hY���]��0Vec��Ϭψ��J��y��pW�2̨j�&if�Lxw�Re�쉲7T������4�c��(�Q�^�����e�[����L�)�7|cnb�PSg�9�K��&)�x��ȫ��{7cn����Ӕ+j�;в�
8��*�����`V��a�#�T�v�YW[�6��-�"_kv�"ZD��`�g�A6�~�f� ��.R������-m�a�,z�����&�Q�Y��l"A3���u^YW��m�\J���'�2�4����&F2�^��D4(;l�S�Ԅs[n�9p1qdb>�1ȟ�`="��?!�{������[#|�nPt=�u�?�?·��F���b�@Zr�pbe���D�>"y+�Y��U�za���T�^˅�g��#�%��P�bsc+�?|���?�y�f���n>���G	X�s˚>5r��梂*՘�'��밖�
'*�8P\�����I��v�uE���k��*�^���}�E���v������q��HE?a9�J��:�!���Ф8�d�gTjۊ�R��YD�kb{.�x��� �a��n�;W��ı}��>u�����	�{9�u��� ��Z�"n���}��8l���4�jrl�U�4�x��޵��.`���GAc���C�v�ԛV��"��7fe;L
�Ε��ub)����ߌ�6�犜s��x�Ji+��J0a����:����q5y�"mrp*�i�4�4��8ݽ�Z��K۝�zx��C[?��ӫ&�s궄�m��q�NW��s��j8^8 o.�n�ʛ�%���6K�gJ���%��	��_�qU-+&�d���e��zs��Y���.E�:�OD��H��bM �'�����Ҿu=݌f7K�Ƅۯ���@
q�h���: �N���rK��~0��774��0�����;�) zi�0�e=��� ǂ�V�0���HT����T�����5C%����
�o�
��e����;�0uu@'6�z"n�	�!"���ք�洩���'����h��~kİ:���&���e���V)��K��Йs+/+��L3?���M�2�3Rf�(u�+w�~�zqb'�M�0�S�|\��Ͳ�V'����%�)y+:.����eXߺׯ���P����e�zr4���#;����JH�`o��ٜ!$��p��$u5&�Y�����Q��-�.���:��}韰4.������iړ& B���$��w�5�>��kWX0��.,<���(�m%}�U��?Y����> ��������M��TB �F
`v�'O�e��O����:+��㎽��4��?y�i���i��!��q�)��P�f��[љo�\�������P�eB    �|�F�=6���Ӄ���f�%�W��&Cƞ2��&�W}�R�S���l`�h&��rt �>4feOE� ��q�c�gq��6v��@��u"na�-�Y�F��Gn:�ʭ�T���Af�EhC?�\�;�k��Ї�0�M���Y��mq0A��t�D��do	.����� ���g��s�!���R��n���ܪ,�:K:�=9`F��2�o�4�[�U'���w�i'���Z���D�U��i>��ae g�+�z ܩX�T�R��p+
-;�����=���&�!��`�;�;��g��o�1Zڽ�,̮	��Y#5�Qr9z��*�C�b �O漂j����=�+��a��3g��mK�#? e�<b��=c��LU��舍��� ���c_Q��3���`�O�tr�an��|65��#�/����Lg�H�R�cO!�����V��e}_O��VQFU�|zst�15�v^��u�+��`�����������UH细O(ňu5rVt�\�S#�Ԟm.h�P��ö��ݭ��C�_ٛE7��n��&)M�6E�+S-*�l��f}2����С�(�3搽�����{{=�g�6�F����2�n���c�j1[�IŞ!L,s��C��0�B���o��)
ߜ��y�OF0;Sd��ٛ��N�4�@��g�kbb�	�98��Z�w��6xi�PGM�:�k���7��������l��/��#tV<��y�N:3���=��Y=+n�C��~?�o�=��,`բ�kD=�����r$a��nD#c��U�8}�+A[�W	em#���Ƿ�8TK�>�>�h���,c8+R�7@�
�V%�U�	�&�B'�VR�*�_��9v���k{��xW�Q��������A+I|)¥��!�ed$u�L~Gn��ZR�I�d�TO�x��|����43&/���JYB�8��\S�^U�~�ΑL����l<�����7��ĉ��A9G�����Y(�vB���s�W���e���5x��1 �ft��*V�����7�oz�5vm�I(}��y襞�G�p(ƶ�T���I`F�=�D�@�&ׇ"MjV�e&\DV#�X����`������~Fk�%�X#�fЃ��e]���Z�ڇ�K�Z�h�,���N�$�ݢv���S��@���Nf�?I�b12�vd[�]�����rr�3H�� 0P!���O����|k2�_� ����aaZ�Oޝ_~�u��nA�	�t�,�zYA5�9�!vJ���μ1'g�
w���������G:��-��7�=[UWV�	���6*Kԋ
��&ssa��X�߲m2���l�*�/���l�O�8��ș�C[��vDW?� ` i��t9-����9j�_m[���V�m_}ù��L�y�����ųf,~u<&��e���t�iH �'r7�-�X)]���N 澟nV���|�:���(���'�1�n��i��n5�6G-�ؗuտ����9�DsO�&�����YM��^�̀��,a3t�r3�9�q.�_��9��ix!o�H�O������c�445f�QmH�V��b��N��}���V	�kCOR{��6�����i/�G.+��P��|�X �/�EՉ�����Yy�.�)�"5��Du��n�?�B{���<�� f��3@�*Nt������;� Hŭ:��bj2�N����$��v��<`��������M
AZ�?��-�i��<���A�-�s�ŋA�U)��K��a9�!�N/�# C���.<١�d�v��!�*b���&����02+m���x�A�Y�V��7�3�Y�(le���܈��~Hk��	`㼗	P�X S;9��� ѓM��K�ևo<-Q	��I���.Dj@B��?��
nK`�m[�g� ٭�q�l�wF�bX�o:r�8�J�s`����ZV�%0؂�#�?/����[�ot!�z��.ǓHt�b�Y���<#%��):?�R.u�gC��V�˨.����|��Y����gs,�G\YbX��׸�����+Z���3���͎�;�^�z�m�-|�_����Q�2g�Ҙ?���V@�Z�}Y���>�,?�] �.�Y^���Ty9c��!�nN!a ��%d���@_��f�̈)��+�7����r��Br��!65�ny�_)�}��NM�;Xz�*^M�W���d2�\$�����h��#�w3P�$>	o��5�x�T=~��e�Q��zQD�J!d-ò��DP`��W�ᢗ��0D+̶��h��C��,���r��&�m�U��B��&���D�H�­q,�ٚ���6�����8��m���ꟶ��Zoy��W�a�IU�傅��L�| �_5�>Q�i��޶o���PA.���FFӞ��XϊJ|��'i���~H��-��8�b�y�"X��,:��/)P�	�|�\7?�]N��!?���������7���&���zO�ۊd�6*���u�L��9�Z�yM��I�0;/���2��`y"�(�P :��<7
s��'���4N�I6uCq8����eM#�����E�F�RY�a:�,K�X�D�n1<&���Ĳ����XV��¬�|��H/G���V����0���Wn�[#��&�4L�@8&趟Q�e�NԲ_�}I�sb,���nj�5�;P3W�U�	�jJ6$�����GTm��r6^Ã�Ggf�'�ؓ�կ�p)^�Y�}h�C��G�C�UeP�9TÓ�\/s�����&��Y�Wi7H�H����u�f*��.���/q a�P`9���Wm� xGX� �>h�%w��¸ѩh��Ʀa���t���R@�p�xD0���	f�`6���6l�A��Z�_"d�ϑ�'%�^
�Ex%�K��ӊ�/�Z�3[��\#�eg�n���d�V�me�V�o���Jɳ�R�Ft� ���&�?m�`��1 fs/?��G�����2��>$Wpv�Z�����y���)����{$~q��JpSQ-�����{Y��O�#��"��j,�;B�h�>��1���I�}�_�\��<z O�؎�?�rd\��68g���9&�K�bu���P�
�'���f�v���F'뻷@�Rv���u�p6�Pl��Oe�/��M�}�K��e�su�U�2L���'Xի�����d�>��OFh�.�2=@ #q7_h�A�	$���*Z�'{�d�pa��<�_X��gN]lyLtJ��Y�'��f�]D'�]/Lz�" B���o.?�so?�������2����vQ�8�e�=�Pf��gE��m+yà~ё�p�r˙�,��;�N��Om�CH&f�����WF���9v���eJ!����.�[?+�������ca���������w���b	I���]❇�`�x��+��!�<��v��D�~t�����i���s�,Lw����
 ��b�w�����V�0�]n
Px$b��q��v+z���i̕�=�\����̔2aPh��])!��Y����8�ޛ��'G��p�y���G#�2g֜��(�B	�������0�굘O#(�eWB{����gD.�rVj9�T^�*�32$�AYO>�Z�w�R?�^�|�{t��������y���e�|�z��|��k�ԏ&��i�rH��ÑQ��˟ 8��"��Y�����n�q tXG�FU|8]��d�ǽ#(�K1����Zv����h��֦"�Q���dJ\����ç���2����ws�c�?���Z�l�s�S�hUg�X����G���Y�8�)-Q��)1*^��s++��z��h^;���fiW���^���^�af$�b^����,�\�H�i��������МL�������������ǋ�p��N�5A���"���7 ����G��J�ܩ=򒬟d{O�Kf���FnÄH#H�D�D�s|��=:��,A~#�Qq ��\�A%zEYN�,'�x�LLoH����ӄ5!����y�#�O�N�7!��c]NI��\�؂f K��&;tr��@��    �������֠_|��QPdOھ�j�<������q�1�B��9���G���=?�ܾ��Ҁ��ZX�x���T�F����'o���r�xD���X�e洭�m�$Dq�o��v�	�ĺ%���]���.�|���X>���[�@y��J��b�����9�/��U�̂�i� ���2�h��阳.��� ��kx�=�o�S��@-�S��g9��sS�#�K����Q�<�٣Fp��ϊ�����C������<"]Q�[;�0D�In/֎>4[���h(ߐʑ"2���9�%��.�ś�&C�������dh�O/���L�w�CV)��]�*���U��	�Ujn�嚓`>�0+�β��_��l�_���7��_���Zx�?�\-��;���p�G�Q�]�~����t3������
!�@�E���'��@qR�t@G�L�2]����J̟ �_[�ܚ�gTYk�eW�ߐ(��(�Y������i#�_C�؅�,�(;-"�Z2gK�&�ɀ�֓��=[S��Χ��{#Կ��E��%�a����
��	R� �?;�\xZ@R�����#r��f���Q�K�י\W9��Y�W����H3Z�,��zv�6�_m�N�ap ����թ#����@�J�B�� E�	���,�_&���g�L�K'*/�����)�2\�!q�)5/�����]3�%s�?��tkD�E�N�k�y<������E��\8s̬���	�ψ+���j^J�9d�４p����ڥ�z�fE�����x=����cL�/3��`���L��� ����Y.n���,'0ǀ���K'����ޜ���;L�4�ھ�g��Q��mo��'>�b��mz�A�� �/Li�E\�8?��,g��8�^q��Ob����h�׊��h��B?����*.�*N4'�+�[M�y'�d�O#G��"�q��F�bl�0��%��J����7-�y�`�~��r����~ �4{ �
��+}���eT�;<<@��E�cs��~!��L�������v�c�����=G��%��7�|eoZ��}���?H�&���M<M�@E̵s��z���=����7�ԖJ?S.�����k>Ϝ�P�m��M�b�a���{���$�+A�A#��ԑv�$�HA��,�q�w��� �w\�zC]�>��o�Ju���B�nn�3 up����Rk���~����{�~�6���4xVv7[;v��5�Z�t1�a~��V���	�q�f�`s�H@��J���Dp���i=�*z�<��Y6�����9�W''p�?��������
	��J0�ݸ�bOi^��:Ό�?�Z�z��Sg�X5w&J�S�0�9��E 7�:Y�b��D��f�k�^+���>��B~=�4U�&:}�2�N~�ѫ����F�ɗ�滹�j�z�8k
�h�\z��'(tA��v��`r?�gEm��%xl��>n�un�-!���ql���<��΂��T��Xc�L޿@�'�Rv���˃w2n��.Q�&ӱ�Q���~|�O�����p������-Y��-�H.i�c��q3��g*�z�~w��a��Ν��ɉ΄�?N�rA�$�F�l�F�x�\��r���%����-?W�껹Y�C�O�[#��}[1< g�:_�L,���,�q������o�(V U�A;
�����Ng�Ī��OXa� ��!b��Y��[�$�a��m�b|�6!�fP�Z/��`��B��1�#"2h#Z?���"T�3/��v�{+�v9�y�(L�?�C���j����|J,�+--�K�i�؟w8�Z�[v	�̖�����f����(<N�%�nϷs����t9�7�Q��-��d�/��g��Eю�����X�ӯ����y�ٙ��Y�`�V,�_]R���5
�8���r�='�9��	��D�p�zk?!�ֲ��}�xl��.Yrȼ]1��q���7��K���4���A߮b��a�p���]�~�V��qQ:� ��1�� �@��M61BO�c�v~��4�9���E��U��p�H�r#���;���?�������b��P6�e߇w����� ��H��ԗ-�P8<��F�i�#t�uff�3{:���:T�k�uwI�{f@l�*؊��pt2Ұ����=>N�݇o�5�p��O�>��/<�Iұ��l�����~V�{&�P�P�ءW����r{�F�:��yK�?캘QUtĎ\?#}7�1���h6j�p��5��]g���R?���!ʋR���D{yC_��FY�1�><��⊵5`ɧ�x�25���۞���X�y��K����p1w+ H�K��B�%{n��]���0�i���[�zA��l�j��cC!��wY
����}(�A?���bv3��{���jT��ANٶ�������%j��;#�#1�w�hPV��o�;sgA��u't�m�����0�ѻ�����:�Ix�!L'/#(���Z�P��^e��bQ㮦6����=��5�mG�0�kۗU�i9��Y%�N��ĮŢ$��-�C1��_�s�����p���B��%`߀�;�<&�
�낱��F���@�F;jt�ۂ�-�-C��ߴ+�Q&>�,1i��6�#����#�epj7���������,��*�Y�n�#�؅YT,#o/���aN�����1�������_���Q�ڍaB�J����W����S�?�o ,p%�!P���Ƽd�a��m�)���] <�)�?J�S��ɭ�	��}J��wZt�X�#XR(f+""Wg�z^�aܱ=�� ک� W-�s$.vq��n���c9��J\q)�}�ЖN�Ē�`��U���D~���y��Mҩ̀~V
� ��n�V6,,�����p�@���D�9ę�X�^GO�v>]IXls<0���^�=�KR`���>�#�]>�oZ��8k�����.ӂ�cСuZ�����l����=��>	� ����y��WmΎԢOKnT��1�T 	��*�YV$��{k��k�|���S���zs3�<:5\yķ��L���^����Ӯ$��0ڈVZ˙6'Mf���,�DcR@�w�ή˧;8� ��_��~�����0m�z�W�8�%�|Q:<醦��K#�)9;��b�F�[�t��lF��=����8V��m^���M/ԡ��E+�!ܻY�������aN����Щ	��J��P�3�RVU͹�+;6����1�wAX�iA�rH�W��^���\��"ղ9S�!aom��K��o����B�У;�L�<,gll�B=/�*Qj��t�g�Tu��]9�sʮK� �X��kr�g{�pr˱��<U����>MF��GGsA��65xz�M�>z`��<����(;�"<�O�"���O��,�%�DD�"l�l��9�b�����^q���������hX�>�*��ESs/�e�(K^���]���/�Zۜ��$$XH�A���v��c�t9�X�<+��4F	,y��
�#��7^4�Ѯ��ﺌ����g�^f6L:�~��\,s�������uu��
�O�?��7����d���I＊��\SP�(�
�%F���Q{�n%U�N�ac5r���G���^*���5��s����y��g�`o\��̪U�7"c��;������~�N;rh�_��W�� -z��^�Fȇ���N�C�S]ב��hԈ��!���� ��Tp]P{@����S�9m��Qke���[�N�]t��)�j��r��A���h���c?�*��T��=���$�\(�,甔�*5��ʾ����р��VG����?c� P���[/S�$3�z�,�Hd��g������s��Pt�H���ӬJY5�~6&���|�@�[�PP>�F�)�Y^a,#Q
�t($i��?���C-��A��?k�3��I%g�P�?�J�P\��	����,�-(�Wբ;{c��7�8�Юs8J8do+�e��"�h��~�BB:���޸�Ad���N-����yL�˚�HN�~V	�S4:as��U�    _4^1�˚Ss6zJ&��z��l���̈fʨH�*$\�,[�ɫ����� �8��5�@]CT7�hԩ%&�97�J�S+�V������?�B���6(}e��2�L��e�����+��Sn����q�:.[y���X�DSd<9��ѷ��K.��I�y�y����jO�ij�~�l|����c����Օ9���fc�?'���6M�..�I�Z�ta�]���b�N����c&%��WSﷂ|���z�Jd��$��UlƝ��������}��Е'�<ԪB{5�����r��%�R�0;������M9+���P?8L!���$W�wѺ�w\����5�T7ը��W��L�t�Ƴ�`�fU2KV��%/N���%���ҥkl\N�߮�ʪTJ`lN^X�5'V����,%���5�z�5�����G<��f����� D��	x��-s$�
�����x�;���̄��Y��q�8�̾Pن+��iLl(��d7R�e΂��(8b��)��hnQ���L\Sy�TSxIewpU���R�	:2�y�ehE6&k�'3��[���&JҖ��4��R�Tܠ�!	�WA2��u�e��p-@���2fn�� &�$FrP�Ƅn-��.�<QH�Y�q����D�Oh"�������k|N���.<X��b�_�~�������k�����4̌���yͣƠF�zy�,�"f'Y���y宏9�u`��]$p��J�F_I�ɩ��!�HK�?6�|x$���*zA��$q_�j��{�:�����_7��߲�j��Ϥ
��l.86Pu�81�0�<¶�^��9�-1�c���L�O�����B�+���U�N�ʍ��z-�E��Y�y�P��(�v���M�J�����$]��d�+S�+)z�%fO��W�������`\���}�/�]k޻��}b��&�]�'���k$�0��ڵ �vH��C>�8�w-p�`jE��<9.��2��c�{=������� �y�X��z�J/�ΈS��e��e��e��������d��*+����p��8d
�����Ft�������@��J	��-Tp���nq��W��k�%�&{c�	�P�`Y�y�5�s+ѱv���ODpxѯ��
�g䰎w�֙��<�ų�}���<7�
��A�c�S��{%�֫ ��J��ć��
�Y.R�R�.z�:f|'�:�8�z����������0g�?y���#a�Ť��N_G�ު�Cc��.<�/�K���d]�0M@���WY��KX�ьhz�1!z��| ��������*�r�� 7��)Ohd�TBӐ����
H��6Ϊd�M逐�O�n�《ҍ�(����R��Wj *�ciK8p��o���N�
�_�u�ާ_���u�,>+�@����#�<F!w
Ȗ�xqx|�{y耍{g�x]i�ĕ�h��͚���p�1x�9PJʺ��ݱ��J�"$^"�p�~J^H*�n;ˠ�M�@�͑Ru�	i����O^�(��:��J�0	���X��<�W��×�1.Q4��g�{�pD��KK:	0��VP��1��1Yf�k<�0�����fS��e�=>$�S��W.\m^�k"]$}�῞ 4�	R�n�u�DL��>^K �`����p;��jb��hw�����Y{]�Y�ؗG�#����"��f��R�݋��Ct!¼�4`>�g�f��%G$;��I�k��:��ھ�����������6�z�u�u3#�Ȧ(��ߗL�o�\�עz�'f�yr�Fqs�5:�Q����i¤ː��i��~�.x��a3�GI�'W�i�/8zd�qv�j4Ķ�*\�բ11̮�V�yx೉�^�wN����YB?��5�J���sM)��Db�����⣙��Z�h(" u�`�5/�C}�����r��3����W��&���������*�m�ЉG�c:1JX��@�]n\�[[�U��yF�p֡8��̗�u��/'�$�A�<ցV��c��#��*�U�O?�ŒV-
�:=�(Y���8�G����W����p�D8��)"�D�篮����t��=t�or�n�O�x��N��U�#�b�w	��1�GJ�]�|����!
2�$��'����ꩭ[+�`�A�?�d.$�HY.���u�2X�~�����.r�����/���eֿ�׶��-���
3����z��Qdϝ"��˿o�8��0��ކ�������:�L���&� q����x\�90E���������X{�R��c�	�~Vn��,9�b��!��֪�-��blq^u�^#�0�������$yvF�h<F�6�DXD- �+�ϊ�N>����(�I�0>k@�+1��K��p����u�Ir7�g��R����I���%(iUC��|V�H�R���J%$�ٖ��O�+9��G�������
g���9�Օ�n%W��=�`1{D��݋���3~��3��L�����i�\
��4C��9�P�f�
��>NB�q���<��#{3�}�$���bx}�"���|��[��}���e{����׆+�$�k�T
�H�^N�����,yupy�1{��N0��sb�#��ѐk�}�w^g<Ri�>�)�i���zž��:�����)m��/��;~�47��'���Ҁ8���@ �C9i���ef�3,��O��PRK�hL�'}�����M<I�hBq�ͺć�����L:�{An�;�K=t� �v�� �/@ȟa"�x���!��\%>�2�+�g���Io.q���`ge����Ro�\�y���Sqs���KL�>��l�9i���s���j�X�3
�nх���@�Q)(�h�_��k�7e>��33�K��{c�,X������!�kJ<�p�%%
�/*������"2�98����9�T#m�\L�o�v<�6F��Q�m͆_u�	��)�"�톛A8�8��-�\�<�#ޙ���w�Id¦&�Zf�F��߫����8� ��J�*6a8��s�:w�u�<Ʀ&<+��~�i(h�����]�-�
]�.8�sD�5X�/�^<̦�{��#1��W�0���y j�K�W]��oՈX��)T�g�n+k���ᅗ��J����'7����#���L�l�"$u�gR5Ϻ�K��%��)��K����A��VR@Hy��s �e����柷�$ߧl�� V���@��u�w����tq����Y��Q����ȟ�A����>�Ƈ�X[�WZ��ڜ�3�/��4-~> �4�PS�!-+��Tz�庂>�#`�������+��C��;���R����؄~\��~&%�}���b'|�ڲ!Y����.$��E:�23��Wp6����G���,Sۨ~V
�L:��`��m���Ʋ�~���F��<�l0���v�b0y�������3�
]5v�v{��T�f�a�_��ELs-�T�Jω��fa�������y*!�z'p6���,�����w6T�k�v�7`Q'%x�?�<��e��t�2�8w�vI�[�2��d�$��R/�RΉ� I
^w�����L����&���ʖ���q�%;�z�Q���!5t������ ���Ƅ	�b������n�Ǿ��gY�o�wn۸3e3���lYJff{~²�sb;�����k�>���\ϧ��ѲG����7OIU���+xg�6F��"A#[��%bX_�Kr�_��$�HJ�T��=F7��}<4[����Q�/���1jv.��@:��1��(��P
l �.�UW��iD���W)Z���o�Ajt�n�P�;1|R?��Q�O���; �3�_��K�p��b�d�a�yH�0���d�"��P���l6�*��������T�Xo_?�D�U�j��Vl��J��`�W����X�{�GE^߽u�OI�����
x��6r�ϙ �\�����X��ovЫ��m�j���R~D3�������!�;��y�_�S�wr*�O]ͧc�}c6�	!cTǀ��GI��=���P�nb    ��\6�N���p���7��R�;"�#��D��%�����+�]Ӹ��k�Nң���%_Wl��*y�$�&Xγ;���Qm�O����)���������%f/a]K���B�J��dC7��ȂU>�;�y{���\k��4��i���艘L̸�"N>MG7x�����dw�����S�+�q�G��A��E��,F����^J�O{�pb�e<H����]�-�B~���OyOV��/�C��n���Xa٧�m��k_�k�d�;�@�bpk�|I�i#�Ƶ�� Wϴ6f#4���Tx5@Ԭ�Gx���g�� ��3�����UB�d�F,u�S�=zU��Wi�bB>�	�m�e�VݤUg> e2���b����ľ�v�>�-�E�/��>��C�̲+�||^�O��4L9��Y��\x$�PN|ī����RNl>Ōh�`�����~P�`�ޫ (�۞�4_�C��|��W����]�o�[LXd�R�:&CeɹqXCN�#�:`�*�xc1�0�ގS<�u�H�D�	{�z�`M������k��\E�|��,A���I�d��������ć���6��Tį�����/4��BW��:�꧵���X������`��pAb��KڃQ��Ǥj��B�G�]��Y��d�f��f���������Z������L����2�2-u��
�*z��{6��-C|UP�
rbR��ϫ����D�qkm��R�
�ӓ�=��_P��rB%��A�5�쭃��a:C%�#g�FqƄ�����'��7�((8PGɻ���#ϡ(\��d���}�3�Ǌ�����(��G"�b�������oU��Y��Ӥتlh��?�G�����G<�N������o�!m�tL����8t�r��/�5��/�׿�BH�0J�X>+�&8+UA\��M�c���I�ܴ��=��Gt<�j�]��K���:ᅏdy�5ׄ�˭_�Y$W*�A]��Q��C���
X|�D��0{�.���p�8r�Y�$_��/ޏ�yۥ�ZÁva;a�X(�)�w��� Ue�����^��v��/�F��\c�9�3� � �:*��|>=a#�s�_���ӄ��1�6P6#��
��H$f�D�δd�w} ���%ŀ&�l��=zchYFz�'u莍E|�b���M���Q>a�bnB9��%��2$%��L����o����p%^v2��e�	c���5c�!��*s��effW���f��F�����1�|�������&K�GOCq&�c���d����F�d~�LU�h<��f��� ?^춰��oe�����c�O��'"��h�!P,8pF�}�N������}BU�
�������Q�p4((�\�����Ðk.�UZ��� s�e}�(����$���������)�\�zw��׃���c4�!)mGǄ�|���ҷ	�C���p�˦���T���(
ޏ6�qlp�5��<a&�H��%���.1Y�\8�|^,�z��pm+!.	��[2��@G*�����s��NU��TxH��i���YY?[s�)�FhP�=i}�Is^�tZSh0��)��k�%�0�S�_�(�-�����'>/��K=.WC'䡯�ej��H�벿��o�!�4+�$7I��,Y$x�>?L�C�z�L���� Jv ü� yu�Pd��n�g��D����M>�,M���V�u����.���Ig��	�x³����U4�8�ʝ^N)$;U��:9�53��wpn��Z9�+�*�N�U9E�&L5m��xT���
q��[[LV�'˘wS�qC���w ���gG���>F&��ı����b$R���F�
��(44HX���o0�3$f�c.)�5yF�ĒS�U���Hr�IF��C~{1�]�}c�]�-��D�\�0��em�%��/ã 2	�1[;���'��XQ48=�&�Y���n���A�'�D'\�)��z:��90����i+ΥNDz��) eH��
F3惂��l:NN�m�������:	����<�v�V�x�Ge�эg�A(!)z#�e��_bO(��"K�p��9��XN�燡�`@���f>�4�ʒ��b\�������N�n�S��a�<�78-�%���Z3�l��	|j�b��Z�Z[𓓡����_�"&�Ԟ?��+�g���{mA���%�0:�����]&T�C�9�m��
�(�Dn>$�H}�[>uz{�5wJ?�F܋̶=��5r��<>!�a�r��aĞ�O�A�Z<�g�����rx[$����eyǽ��#h>]��6�uڥ�f&j�I�b�1�	�{m��џ �2�e}��5� |��=���Q�NP"oy�қ������k2۹�a��7��bFv��B��ug�C���h����w`OS=����Q�O�$�{�޼��p)��K��]k�ݎ�"ŉG�vQh��١L'1!\[�/�	�XMza�H�<:��l"w/����h���FJ-!Ԕ�qC�7I�TzN��N��'��h�f צ�^QYw:V;	�r��G?��X˰\��]v�|���2���r?���P�s���n,��0�"��B�U��&r�{�Y�0�"�p|�e��
N>���Z�w���rm�������$�ko	j����,mG�N�� ��ޅ�<�\�<%����w���6K.���
�Y��-_����C�o�"(��j��~�V]��F;���+]Q��'rRr�?�v�ff�^}���9yy|tpt��Ƿ>�����i��ۡ�m�ˌ�m��+��'�ΒF��d:'�w=�K/c���Ξ�0V���x[�'f�eNզD?���
s�Gж��YS�]!`�`(��	n�9�k ����&\o�uR��n>k.b�;@�)����'�Wi��e+ڮ P3#<8;��O��4�l� |�l�l������L�g�&(A��+x�2X�ү&+�Z�3@3̦�����/����pr?�b?c#��P��p�i�����1�:�40�A�^�����׀����J�9��[�Z�ĺ������G�Ρ��O���Ƒ�=�nK�h����C�$� ���E�[�>�:�c�:�"�m`�>fww.�<O~|�#B��.�����&?���+Q�-���x=id��t��	���P��q�M��=p�yͧD�K=�p�+�n�9c���Q.@~3X2h�{�P`U�����1����+��Xll�A9C��b�@-o���s��s�4�n����VPk�MPs�)���g����d!8��8���
$���و#�s$9�+�j�UZ�9��)�V���z����ҎA�௽C�>���^WQ@�����磽c�1B5���Kʻ��M�jW��H�R�z��G<7樠\=f��Iq��}����[��� e�d��EKH�e����C�@'A�Ŝ_�@8�~ޔ��9==�* I8�`6E�ZT<��]qs�K��zlS���WX0E�Ys��c����;��e:,�_�U��b~F�2BWC_���vB�3YJ��5�~9L��pi�ΧO�D����\M��5�sѤ*�Z���֋���0��	���>z\>���I����Ew�3 �ވ��{�n�@!3z;<f�������Y7�<�e�a���^lE�N?�:u/D��u�E���M����@Bry� �@_��1v���J�\x����4�F�*�"�)f�@?���
�>���^�ղg#��η�E�6_sOI� Y�%{��Ex?\�\ğ8q�=��&�9;���N-&G�Jx��Wga:nhz&�,gU����;��v�W����n��i����\m!"ʂ @c�4���ZhW�M>며|�l��E�Ty�m���]��O��G��1��w	��%1���Օ��H3Nd�Zz��������x/x�=y�u���1�B[�������V��ܪϑ��4�f���UL��I
�	�/�������%����U�L�f�`�Fށ�H�GFhE��&N�(��b�r=)�|l=ICBQ? ��q�.���=v����to���U��4	X��"Ǫ�i�����h8.�a�    p�)!ʽ���vr�4��_�}�E�<�$���Hk<����(2�b��3�����&����vƚm~�;��N;H<����Hd8WZu�(pQI�P�뙝%�H�=��`��FT�Μ�#A�&���4A��/x�4^��:T�觎��9��r���he���<�৖�Rʽ~&2Ӳ���ڕ�ʻ[v�w�/�ɋf'��� ����Er�%��חPn,�&AO#[�R֣�-D���b��E��=]1��L�%i^�ܛ�~	|�?�� ��P)�ᐓRĢ����)2[0�yp[د��d^g��ž3HE��<�.�w���]sC�Yg����Ĩ�3�����#}��=��3�&$d�g���}SZ?+��r�>�����?�*'��������+&t�k~�ua[x�m�oZ�|�8�U�r۴.S���W)�vE�[�����7���g�/�)u�۽�:��װ�K���^N�LT5ZUh�������/W�	�--a�����;ߙd����M�-RC���j`�Bwg�"A'���؆���exl��Z21#�٦K��"�k�7���K��I����{u��Tn��"��'�J�a*zf��gC�k�S�7M��t4��l�X��b���g���O��м�{��2/���W��b��L��2+�����wE��-p.���	u�ǳ�7��G�|l�q�/��^�pC��������~�lӢ�s�A���w�E��
d���ف͂���>%mw]) Ϫ���I��~&\��C�(M�,�o�JxS#1���3am�\J��� ���ܴ�;�9�^���q;��1�s�{��0�L��׉^�4�^����l	�!ꦡ ��4�b�f�D[)����q\T!˞ǁm�2�޶�I[��2R��b��W���4�2+���/M[�iLY�B���M�}�E���`"��U9p�rmU�j�Pe(�v��vv��0����GaE$+��0���%�:o�H]����4��9��%�|�yn�7����}�L���rUVUO;5w{5�5�����@��5+�T~���\T�s�J���lz��S<�
����~^�� U����t���j�������%���<y�x�ꮊ㪹>eX`���l8��������]��r�0�!�~'���q5J$}�J>P��	�$�>2n��%��:��s�s!X��k'Y��X���E7Xt�͢î�c�$-���/v��z��_�+���6`,u��p�Фy��!N^D<$G|Mk{N�@�|aƑ�0�`{�T���re��F����v��7����%�s���f2W�k�BSb�y��3bPЬ�q`AV�ᶋV�o�~���:��+d�:<�ǉۮ�;�y_P��0Ȯ���v�Oec�HJ���y�Ì��2����N���GH�|�Ih֜I�I�3[�gv;���7V'wZ�7a$��靶������2���>�����n��{p�|<8<�==�x�{��!|��u\je��6�J����lҰ!�nI�5P'��(�aM7��nei�b����~��/���`>�:vX�&猣��]y��;#Ć_q_�s�y|�n�6�p�1�D�Y��\��֐�*��eP;��5fl���6$�/�����ېb&�3��W4/�4�t�+�B
iLmm���E��CDZ4�H3a���/m#������DiL0�e��1������M�������s*b�|~�	�H�K�?�$��
�&�qA�l�0��y�X۲�9�5*FAKn~?�a�U�'+�3�ͪ^p�[�:hզ��hC�;�}O���|έ�}���,�)���Q�'��v��ȫv7M!�U |Vt�=���iw��g���j�3�U�J�`n������6�9��邎�8���c4�����/1S��v�51jʂ���f���G7)6�ќ���q��cE������)`JD�ӄH�g�W���lk7����;	�#\��oƆ�Q<���YY�����r�Ү��`���4a�6Dl8s�a�8B ��f��� �|�S�7Na���2�z#��=����X���:���Yk���!#R���*o�<馎�B9i��Z��E���{>���B�7�I�Ge��v��w��L��(7��2�ޖ�\���A����(,VVA��w���z��~?̧c.;��e������aҋ4��ʮt�F�����7t/3�e`����vz��nN���`�����k�C�񘡋$�00�"$�-������g���`wWI���Ƹ�o�pl�Ő�K9E��5�i����s�mQ�"��_��ʾ^P�.K���%S�r5��!�7Xl�~<�[L����H\Ɣfu耂_����}��qd�N��Y����Ũ�StG?�����ڮ�&v
T)M�Ŧ�D��z�T�c����~�����2�(͟����^_��?���[�!ʡGƯ�[?��ǫ��I��22ƁJ�;[e �ᛴbeͭ�bq�n8HG�p7�w�Ι=��'V�X����m��J���g�<T3�;�-��k��� a�@@���F���ח���M�i�)��՘������$菝�
	�l�okcy�$���w�
8M�]�8�Й���ܐ�Ӹ*�h�
�ɔ� �rK�"�z�,�oD�5g������
V�3yp�G��ZA��Q��kG�����͋���ʕ�<�@�z�ΐ�t�ʕG��y}�M+�Dj-�	V!�wd�C�F�nGZ�*��E����O�% RҘ�تx�{��ߋf�O��=�V1� ��ю[?�伇U������[)����b��������Յ��B��a�A�K_��V�l䡎g1_tf�:�ɧӱU+,F���Gc�\��C�$F���F?�|mGE'g��*�;"�#D�t�� ف��4�EР(����E�p��0oz����;	;I<#��X��b>��ym}1���vK�Yu��X���E�q���R��3����(��Ta�XZ���p�J��܆R�ᬜ����Ҷ	@Ӑ�����"��_�gw�Sb�`|�������}(U�w��E��� ny ��^�آ��>��流XC�˹���NQ��,5���Ѕ�1�3̓�|37b���3��b�!��%Nm3�m;��8cci�/�����5I���^$/�⧬�;h���C>R�!�R���\2y���;�5G����~�\]p˫d��_���-��δ���$1$�e�[���'dD?��U��k��nPU�v�e8s��#]�b������?�36"�»�Mʒv��D���xh%����Oݢm�7�z����%|Z��0�z�qc?��5zv�D�������I���������:[����꓃K��S�'~M{H�Y����uwئT����K.	���ˢG'��/d*�3�K���=w�k�S����Nz�+@VT���Ş�r��f�����Ϻ�;0y��_6�2;k
��Wހb�s�>N��@7%��葓�}�ͩ����%5��'���<g�/��O��\��P���U�����b���Sppgi/}�RIPeմ���'���	q�o˹-[����*�L�nZ���vDE ���?RzY���I>���]j)�@-�0��	����f���k�$�)��k��T���)�1���ע�E�G30�-����ŋ�B;����h�E2T5� =K7(6�;����3��s7ٟ��)�>�����)�5�'\U�f9��>AN`�ɍYj�鞘	"	h]��w0���ب�&"�%T�l�΢��E�u��#�'-C�T�f0T�� �܂���*��8a��U������D�[H\l�0��9h��l}���R����_�U*�S?�pAaw��*48O��#���JN9C�uH���Mr�-�~꼪X �Wݙc�5�OK`q��f&�/hx���y��K�;~���e:5�d
X�H�m>�U�(��#��L�2�5'1@� 	�}>��eG]����
��u|��]���M��#E�8�X��_'G���[    W���g��o�R�rP����c4��`+����U����>����Wَ P�CE~��@ |�����&JG�&K?�������ާ�+c߂�Mm�5%�Q�^��V��(�jcu�O��V7��b���B�G�in;;g����c�d[��S�p��x"Ƅ��>��-P�hZ<�&\�k5R�9y�]>��1�� �nD`{%�u9�EfϽ/��)؍���(�x���
����b�N�K\��֠h�"�	��Z�"z���@�t�\��v�,o�5*3�wb_��$z�(�����B��Hjm,p��G�#�횋����5"B�^y�l�.ɢ��_�V)�U��WN׺�[�rh�{W*W铢�����+:͓�n�n��_A�1�q�X�ooK�Y��?A��fd��Sm}����B�خ����b�
p��d5��1a�y7��xe�׫0r��b���螜6к���F�[�[ci�W��r�Ө�< ���2C�s���y{}�
�?�u�F.�^�I�$<��o��+S���%x�qF�*a��^��,�!�?��-����6����>&��"QF�����j[
��hy
���i��˷�ٶ⫏�k�w���^� mǮ�I�2��R�L)�������_�%�`"�O�u�˰O�}|E��;ɽiJW�%-{����(����v[ׇ���3�a}^���kd����e?�Dm]�r(��Ys�^{�,���g*� ��ͳ�fO���EI�n�P£bv�U�W�9�X7��O���n����
ر":F@��\��u�cs�Q�Z�m����g2��I���:���s:�/�FW�F�91��y��+V�͖^�u��/$J+��B)cj��~H��^B��X�'^Y�~~Cm��C_v4�b�P��gR�.��b+������o�/�`�V��ˠ�Ӕ��c$����Xn@���L��
�կ�G���!��1�wO����������~�4H1���/,���a��W�s!3�77����am�&l��M�a�Db�ڻW����gE9��u���@2���|�$r������}7O�c��Y�?�g2\x}�է$M�i�6PM\�'L�'":yZ��?(E ��� ��hBEkH�5�
[���y|\NF���P�I�m�o ����6�B�8/��n2/��<�[>�������e���^�ʊ;����l#�j��X�I˕E�t�D4�?P��[$u)� 	��R3���'#n�����ᤎ"�}S���%�MG���#8������0#���%�^�{�TK���d�\��p|�W���`sF�M^�T�O$]@H`7*R�~Q��)?�l[����6�1#��H��:��KG�>����*C�f��[���媿��rUL�zOI�+Q	K�ؖ��gb���&5X1حqP��H�L�:�B�0�ۡ���-v���57O^Oq\��ʓ7t����!�S�
u��tlNK�D0�O�'�s�(�6nCLv4�#Z�{�v�80_
z��ؖb$WD�Ҫ`��`⫟G ����i�w����`yتo��O��6��������֡��	?�����c�6{B[���mF:�������}��V��A��������e߼�W�`y�|�A����Ow���.Aq��{���:O��h����������J�_v^?�	Re�3Ϟ�������W�����k���Kw���b����T������Yc^���9L�wn����$�P0���<�ˣ_PQf��\�"G.)��!�0If�*�\z�+C�����pE�C���&>7Q�6� �U�Ln�* N�y/d�ތ~�SDfP˥�.'DK�vܹ���6��D8��P�ԣ����ofF*JY�9��Ȝ����/,�� P�&r����i��'u�[G86p�`@�VXsL,;0��V=S+g&PL1l棑@4"�Et^ .ksl���e(�x8�8�~Kk�>eV9�u�LFZ��ݡ��1��Sv[��
#�1	�M��fL�\?S��V�{�Ix���7�yĹgH��c�f;��N����1u��@��f6O�ޅ�����`2�M�R�l����?�Y��t���Q;]�y@Q�u�@���D���78����gJn�f�a�@3i�XYP)$�.J��LHLdɝUrЄa�I�C���x��d��G��BHϼ�C>7�`V��k�v�pI��qAd�%��Vխ������ ��3>+������+�pJ�k@ ��%M5+�-- y�W|%��\w�����~�²f��K>��`��)��v���R���|-B�Ȓ��o�Z�P�T3%�o�fj9H��2��RZR�repԝD�հ��<�a*���Ƣ�&T>�bR�d���BV���|Q�N'�Y�|���BΤ,Y.�Eba�����g�(�!"~�?���n�g��r�o�،'6q���d,�)�B,D�(�7��l���u�v��i+���8��؎�u���x5_"��Zb1��[���УS��J�^�=������Y<�R�5vd�����\�Q��:��([�&�����I΢�⸝N΢U��_|i\[^�FJg%}��at��F��x{����NE�wǧ%���-&ruUd�@�"�n���@qk�𿏇ۅ���_���L.��}#��ra)^��/��(R�7,��ƪ����g��C�Y,L�Sn]BMf]: Os&�Xۜ^̦W󨢽�Ԝ�B{[�'DYh����+��k
=���2IF��ֽ���W�`X'*��2q��9���M�hR,fl��u����3l�Q��T�dp\��IP�:�yl�C�y�t�;�����z͂R��T[~�Q:bt�- [_>>�;�Ӊ��g��p�נ�`	؀�^j&��BA{�._?m�������a�@��O�C�(�a����ʘ�-:����0�3Y�
��#�;�E��Ը�Q:��%a/��N^�R�����1Ȕ읯W6?8�&[VWh?`�pR.vH���֭�{E}3�t�����7�k��ڲ�Mצ(׻������Z84��O��=�<Zt?"�j��@��mq2��?�C[�VT��pM3�ȃ���%ƃ�pO�.�#3�b�nP0R����M�c?�\ 7�Ȗ�m=Ĳ ?k���D~Vu|]�ܐE�
�~&�6Vj�|�d}��[Y��ڦ.u'VҪe=��5Y�)��E���,��뎁��{��T��+�[)Q���+J]�ǿ�ϵ%6r��>�t9#�:Vo����~������z,|�]T�����c^�K���%����RX��I�둫������z��>T�ö����S��}n{��\���N�Y,�3�о�k�: ����h����TK���K.���{�&bd�x�Jdb���R��>,�2��^�l�}�Z�<��f�ɿ~V	J㰖�(����f��\��f.��p3�b��c?z�f��*vU�[�ة���]^>�W�g�r��o����$QM���pE�F)��e��-)�% ��P�%8�o9J��8J��ݎ��W��3�깢Rj��GI�j���)wЩkfZ�Q��ȥ�'(�N�*�UMM���Q��K����q  Z�ǀe���=8@�~�F�(�_`�T��wwVM����a$߬U�>r���t5�*�t�n�����*y�g}�fuf��<��Ñ��=e�H�<�6�U�]~�C�y��^��������gyo#݄kk�%����L�\"�-yl���\]���ԕW�.H�&/)�MA�"&���OF�����̊�^�\t�=Ϛ�wdN���S������uh<Y��c��M6j�L��В�C�P��[�,d�Us�w��NY�O9�z���2��Z��O�=��>���y��#0�FG��p8�X��t>^R��|7鋽d<Z̆��G�я5��x��@���OJl���#����,�9��ͧ�^٠ϝ(�65���G |b��I��7U�U�{��?޼���/5q�i#+ s1���<�����e�ͤ����8[U���D�}��3����\���gs����ѯ���^� ]���������o4:	    ���K�����n2�|��M-��ڰ�'����x�H�h��ڂ�g�ъ
�]�f��A-�)�����-&�%1맭��0u-�g8����t2�7_ŭ�= )���~�����u⋢�������F\������E]#`�
[%:a[U4�3�'��YPO�a�ԯ��5��gE��!�͖��R���p���x��i���Ӱ~�Ns]�.m3�b#l!�Z��~���#���_��3,1r��p�p��fڇDE�� \gf�X!�Z��H$`��O��N�$O#�0�.@#3�g��V��)���
3��A����.Gt��Rn�f��6.����V��bxgdn�s�����h�RU��w{�a�;���3c<�o�6��q�>����s(�nEz��w�3�1�	��1c
�2=�Nr0��� �6A��@&X�P��@�`����=d��#��wO,�U����27:z��R�Q�r���e�}J3�Z�.��8`+P���kPt�k̓W�i;)�{Qt�׺~e��cS=��,�g��}'���x�.G|���8�9�pmǀ
*����k>�/��\:H >,�aY�ܻȪ7.�� ��#Ԏ1����ѭ��-�h�9&!0��r�DMs���N6� O��KR?.�<�r
��27��9�4�ZB��	��a+;l%���G��aJ�|b��Y����8]hZ@��dp��?��1z�����q�
_�`H�8�G� �@`��B?|�Ԟ�\��/��?�=�b2�3�����:~]��1#��;��wZ�s,�ᨄ���t�#���Ȭf��<��򺆹�� sF�W}���Q̗���\�z
�߅�?Ȅ��*}�y��:�E3y��&�K0��&�7 nm[�@y;r�ۭ̯���xk���
��c���^��&����@M���~�Fr?�G��J9�\@mw���8dRd�����Sx������D�<�BEkfL\�5]k�Kh����5�i5'�����\i|��|�U"mf6��~^˳��i�xup�y�ǟ����K?'����TE��n^�؉kd[�d'[��$��1E2l������u�K�� ݢ<�g�S�@�8 �������bhXP*� 
��A�&h���jc.��I�s�����e�f�\bT�S3F�t��[p��l~�dB���-v]?�� ��Q*��ې!ۭc���o%z��7�{�ʞC��M���u�0�ߥ�LB&e[� jFA�ȧ���YUP��y�9/��2�r:_�pG����� K1r�S.FC�;� ��|6�CW�$x�����;�B���qCڻ�FԱCZ���E]�e�z���1RXZ�p9�w���D)�E���mw �	��1{�
ǂ�u  f�u�(�3�1��`t��X�8'������* j���w�����/��5�[X!:o Y���Ƴi;����g�9&@F�F!$��b�T�W��ِ�x���HH��s� V�e���|�;�L�1z)�d�6ł &�jc̎�b�dbv��&��E,m[����� �g��J�*�&�L��`y�C��'	4לۤX�H��e��Ǟp�B����S��Z�n��3r���1C��@���Q6]��+�����ٻ�c�_͊���=�q^	�ݨ#���A�hS!���8*���<,^?|�ҭYoyxZ�#�����g�;��'����=��<���n�b�q��>�xz��9H�#
oB����$�O��fT��������u�h�E���
R�^!DV�0߉����(`�9俼;������Φj�M?��� �d:qV.`RM�s.'��� �.���
��?J�Μ�7�Wx���i�^��.o8RX}�Af�v�4x���yyMHa�|0]V��y��p��2�}�ۤgpz6|p̞�	���{� M�+�ױ��ϥeȮ�F�w�zv�\#7N����-�`������"�V5#�88�ǽ8�9����F�wf�U����n�K�_�vv{�|49�Mr}�B�7��o������An���W��ӅA@#��� ,�>�����K�.�8�Hd��[����UM��ػ�\ٛDbb�D�p���r��VE�>I����m�xW7���&�]G!�0`؉X	WA�<���D��4*�%Bu��<�"DQ6��۞n�*�ʈ%|~f�y��pqI>�@���.ڝ���`��)�xH�y��z�B7I��g��)b��\6�������bq�R$����ĭD��s=�y}W�0w��'���|&x�&�h0���}�$�p��g��"AT	U����5]0�v���Z�Hjt�����>X1fGlYzΓ�(�t��(!8��TH��ue,�����@A��K��Y@�e�!�;���~��I�6�?g�?c�h�k[��)�ƂAR7���[1
�&=����&v��}�]sjF���3w�ţ���z��~*��o
��)��Q����^/g�Z�q����{����LO{��ٗy����f�+���(�`Ɛ�G�n�Iz����t���<�pe<��d�;��	r�K�Z1�/�w=��|�]f2��K~��kN&и��Ea�?<M|3"p�JW�اu2V�@�ՒX7�}�]2�����eq�]��
Q�^a��O��p���
�r5Pݤ5uBp#-��r�қ�]p٪��az��_,�_c��/G����� ���&�5|T����'������l妲��CH��A��-�3���[�d�Z}�§uZ%�!��E�E���P%�	:$l���$`��e��j�^��z�\���Ź�9�2�|�Yk:��SO,�@�;�Z�Р��+��CB�gz�!�ڸh�(ɻL�����|�K� TGhK�M���C);����A��N�����p�6I��Bs>aO9�Υbd�O��%A��M��c7��S[��p�=�܀O�Zl�ْHc�rFe�E���On�Rg\��yyL�ՖRP~����3�̯��ٓfK����f��R|��5$�{.�)�vKL�K"�JFo⃢�,��/'>$��da{�b���a�
�<�}	����3��%�8��YW�1T�k�)�Pu5t��Ż&V�'o��$�H����e��z���sV\��;��Y7=��4�H�ۏK����P`7*wA$�'�GE��?�b�A�~��u��!���o=&�F���K�
Ls<l�Pv����^���./�\�Κ���1$"n �ȌV��I�N������倽��\�s[u��`p����E	��z��r6�~�����;�q�O��f�	��$=n�e��|���3ڛ��юg�)��TӶ��g�gU�Z�3�_|�PbFi��[�I��u�td�};�D��L��d������2����~6]����C��e��Y�y8��RA� ��:�)l��ԜUx��������CΖF ��Rۛn����х�G=v��)p��휽�4�;(���T�o�dΦ���t��d���Đd[�9�n�zl������Js��\&Y�u3�b����}-�(%���CňF��DΈ��C�A筨 �c�	����,_�ɥP��R�k�� W/xl����#���z����ʑ��ڨ��A�0%q*�_Q:7��+a��H����Hq���s���Z�a�]�곈X8HX ��P�In�I�S���ݾOe
�����G������I��#���O��6��=�`��Y�v��zo��Q�%�/�`���R���vz=���n�Ec���Z�S�i�8$��8p2��U�|�S��%Yru�$���!Yl:��M���$XMR��M�P���P~�x�n��mw��}Go�@S�2)�@��n��. �5\h�)cA�glg�T)����H)�s���c��J�E����D���[g��Nm��h$VW�z{�c��=�qsz3�e�q��n!�9:��M�n�i�㰶@,6vK8������Y� ߠL����.<zWkJ�p���"�J*��y��e����0��{�
D��u����ƎS>�    ��m��#,�<B�ly���:t�U��Qv��A�(�E&�z�ܮ�Ə�ܹ�쪫DHI]RX����'�w$�T,'�E��Sd�H�!���n6ş7����	�Ϙn_��������_ޡ7�}�n뗻M2[���Ϝd@�����טd��m��$s
ɠ���ï1�#�$i�������B�ϴ�.�)�X�-�,�p*���d�D�o�?�B�����<�A��?A��� �҇3}\Z@���$&m.X1�����N�g���E�Ao_e��\b�	O8�8��S^O�ױ�b�>�#��m�*��<�b���1�˸^��!��t;����zc�~��oF�i��G�E��bk1��\�PŦ��Aξ��0x�0ya)��B�{��38�<�<nD|BYr�zG�j����:�vVq8���x�:ZE�&�1Z��F9�D����.~��ޞ�g{Gg/�
�4zZH�]u�b�cu��YG�Г�I0��\.���'����v�9����f��k-ِ ��f�5�r���HV~壮N��Cq�|�����HR� ����:�t:��O�]=~둙h�;f���VT"L�z#�Ӆ�b�!�z����6���:'����-�����8��C�G�e��.�Կ,9l���Y72#��Jl�I��(��L�-�n����2����~�mȷq^t���y_���- ߩ�淠ݱ���{���)֪�l̕g"�����,���eG���w���Z���.<aen��'�IU��J�.�"VF�H��CP��@�h�=Q�� �Hs� D�ϣ�,*� ��ט��ߓ?+�C�`�< ;*�

A�+���t�WP:�?�4�{��~���H�3�+ Ю!);�g�nP3�+}y���Ҝs��V�h�W��Aj�E�����'�?B��������w������-��j�A��K N2w(�F� f���K��������kn�FR/��(��4����9ɞ������Ü���ƛ�N��5wa�|;��ِ1�%hS��?�-Kg]��:L�T�	"7~냳���qet2"�Z�Ұ'���$ ��]��Y�v�m0��8��q<qA���}�Wh��V�ٍ!v���[w���š���Rr���Dʒ��HS5=H�&��"�F�{�䡆�{7U��\N�۲�Nko8���k?�%�eσ6�����T�K��hS @\������;���Wt{=8�E�-�"d\,�j%3�8��'jYH�aj.�W���i���������_�s���=	y��~a�=�}'����]����ls"�Z�kfb�-1��yO�.%���������C���~���m�����X�=d��}�nн���"r������Iuڽh��������5�@vw ��E8��diJ���'�t��w���&>�� b���H�6aa�w�����a�����p�w���	X���̾��s����O�+ )�m����XC&qG�oH� ]���L�<��5ӧq��B�:>����~A�\/{�v@Ű��%�v<�(��ǩ��s����1��]mJ�����.���w�Z"K�GgNY3�$"Lt�5�c��/ 1��<y/�B��s��[*7n�� ��M�Xe�Frb��ȃD��m�@[T�1n�U��k8%��j&10"�	��Fai�rC�M1�#�%�3I����+P�__B�r��M��;f�� �̜��}��Xy�)|?�MSg
�Z�#�y]�3��4Uz堟�ꪛ�#kW��	@�u{y�-��!n�*��e���>���am��%��~���2��l����c���3�wL��X.L��fnj'������3�i�����C�
�n���m�͑�!e#��-��n�Q�rd#3xu
���hf��?OX����\�w��*"�Z����&�?��pt�E3�ν�p�}����tg�!������^T�'T$��D�/ݳ*eN|�n�E/��2�Q����	̹ڗGnW���4��j{��ZB*�tB�$�8_��1��x��vsW�����j�<�Ȋ�r=�^�����j�&�B�W�spj8Ɖ��

�Q��4e�wU�D��<�3�@�$6�o���z�5ۃn+��{CO�L����nD����q|C�cK˖����by�@f����e��d�AQ��T��&:"�M�E/��W��n����r!I�1 xO�α}��Z�^�J��?��.���X�Ը��Z��E��!��Z�I�fJ�Q���b���_�����=\������|���o;q�
��,�7�ٵnL�E�l�v�c�>-D0w~6��O��*�����Eײm��6-BJN��ls��?}��������� 3s���Cw�s������&9f�v�Ǡ�{���6�j�+�Y����g_ZV���b�η?�O
_�*�S�H%�ųs1������v�⚛Y��b��d�轛�z]����PW�$���ww�6��������7���;X����%6*BR�AS"�ء�S�'�(�H�gK�wǆ`��ω��ڂ�ǃ:��FC=�S�]�!�	��(�Ȝ	�8�ҥn������,Y��0��W���/Rb�[V��Ə��?g�Zo���͖�V b�-�ue��N�J�B�$�f�u�J�e���܇�*�@l�V��<h����
�����F��A�]{]��0F���KiXY�U%�����2�Ґ�g'4��8V9�YO���]��x�N�]���<�í���P�`?��0W��g�h��˞9�T�B�$�l�4o���uʌ�u��m�'ٹqO�g�~�ʮ
�i	��^��D8�~T��NP[!U�~�4����o�0ʴ���My�i��T5U��� ���R1���e5'
��\ͷkS,}1��ux�黓6��N��[*������f��ye�r�"r26}��	��������d�=V�ynm�i։�&�U�Sa����ͦ�V=ú�/�"��'>�]��h4�6�%ݦ��	��-<����.p�F.b%8S��d����d���1�~=��]�n;��F���e��[��ۯ@c�j��i��m�Z������tT��o4��Ç�#�w]�m^��^˳w~pc(�/b7�C[-X"Ě���=~��Gm��n�����0b
X&�Nm1�:��B��;�3�4��{�,ἑ�������-��N�t��Fni-��m �썬���]�@��=�z����m��myϣ������j��Uv�߆��+l(��B�iw��iNFpGFL^̮�>�п��jt�#&�������9��.�F���n���h��:��qT���������G�gſ��x����	w¢���n�9Gnƞ�9�6���o4��-٥�@����Iox�9�vN�?6V��'ǧ��Ǘ���}ua�^!����{�ݴ&�Ұ��ő����.�˹QC ��������F:��~'���P������6k	"Q��zTr$j\|wyQ�:б|�8���w��iOc
�����������<��B
��.���8,�j �H�@��!��Y3EG�����[T��f�+u�5������<�ȕ"o$B�:+584_�>�#G�Bbk��� �~���t�ջ%r��Tr��ϊ<u�r��2>#զoEtYY
Xiv�p�x��B��0�A�,* �z����)��eP��:w��@��k�w1)�B��ܕ�R��u,ޭU�B�ͦn�[:S|9A�A�1�1��+���Y���(��v^��S�%T��U��®!�{����lb]�ՁzB[��\td��g ����R�Ta�5ݨ*ˑc����_�ɮ�Ӧ��tELT�öI�1j^r�9�9}���E�?d{Q��m(+�n�n��/V�؂v���M�M�ɚE�=y��$���n�w�Q���ŝ�u:��[>-iU��vz�E.��1q�����3�ZL�l�T�"ȳr�Xrlk<n�y}d   �<�」���n(����Y@��jp7	��u4��!Q�l'��a'�����<{>8�׋�B#�wDB�4Q[G���P:iS�՞��ea�AI�>�]�{��\/�n�K�
�Q}VU�a�I��<lZhF��Wz�mT�����^Ϯ�K�4���/�(3��ly{���/���HJ[lA�1Q�1��W�g�/0�!`\kWH�,�������}b>u��+��˟}�HOr�zg1~ce3��HC�"�-gtb�$@���'贝yB�u&�&�­�w��{�d��M�n��-��}�_N���{N�8y��)�kÝq�5��E*��Bڽ{�����o$НF�2r��h8�BOe�Q|�c��^��޲Q	o�1���s.q@pԾ�ȝ ���є2���3��e��x�9:dq�S�!1�Mf�af����l�N����(�WV�S��J(�@�{�.���
hP���H�B��d{�����ݿ�����e�Dt���Q�K��e1��#ѴYy�h���PG���J����	X��|��g����_��kQ      �   �  x�}�K��0F��W��T����I�0��4t�	m7�1���g���m�ϢRY�s}_��"��(��$��~�ߚw'MyE�3Ӱ麞E8B�e�
i <�;��Fs)��7�52k`o<I�1h�8{(�1PZ�Pez���s����%��*�=�Z��uo
�d*h�[3%hG�h�:�������gT5�ͨ�+�K,�y��[M��ہ^蛇	rp���}+��S�Q8��;73}7�����ұgT��>`ɎGf����4���hz'�	x�n�����Jn@<�K�FxC]^�!PHm�����Ը��ja{
Z"ɀ���_\��(Fϟ6���./�^�vVJI4��������o�+�'XmF���겂[��;��9�O*���e4��$������b ��������&��S�mه7��(�Y���))\J��	I���r٣�Q��P<3��o:�x�Q4����d2�۞!�      �   �
  x��Z[sۺ~v~�N_�W��L;���=�DI&N�ڎ��`��D�$e7��� $�$H�����3��-���./����(�qu�/w��)�S�/��XdEvo���T��h����K��.ؑ>��E��S}�x@oR@����I �e��K��z@���!����= �j�c��I��{�h5�@��	B����wW)�%�ӟI]�5OYen�0/��|���$���9*�*��y]��|6�yݘ
x�1��B��.�R
?bh'wi��q a?�R��f���*���1 TR@��څ������:%�+��o(��}��� ��)�ŧ�7d��J�<`H!�a�湭����)�X��� ӛ-X�q�)�ȱoJ)�,#uJY`c��"(�gbS��^� ���"NF�i 2ş��e<�� v$1�w �#��Ã��T'g$GA@a����9� h��gTGW�/@g�8�A4)�Lz���QW���������q�5��r�*Nyq#��"�b4,��]zsJub�Rz�8��C�������JB�����7QˍCVn��xF�,���Q_]��h@�)����� p,�q ��HL �@�Dr���
�/R]�w|�E*�,�Ɋ��]e�!l����*ٲ�R����Ͷ�ž	�(�_�  � �#c����80�{xh��� �@HNl�.��;��M�2��R��̵{������M~�/����9.�A��!,��.���W)���-�-n�旳ˏr���������H��̈P��Fc:
�γ�m��|3�K��+#�, L���S�Q�ȑ��iȰ�O�	��$'p|.q��o�`�W�G�rj�Q�� "*�Y�)̓���p�<�N'�h�^��h��=��r��e�^�e(q8������T��w~�QtO������y��Ûu��8^?�r�</���\���ǋA�g��S���ǆ8��g^�'\~��h^���g���Ƌ�w����/G
�I�p�ċ��-_��SI,��>�)�_�%I����^Zk� �E�o����ll�"IE�f�< 1��)�)i��%ᶵ����c���Qj����_�z����K�w���ؙ +��^�_�o�U��_��h��
����3X����̍�N�NNH}e�"����gp�'�nYޮL���mc'^�6��ڐe�+�j o���;YA	��������M~�\�E�%�f�'c
X���Җ���o+�ɪ�u��]qWV�"�U������lnݚ
�T�X���;�'3u���?nM�.o���0L5)�P�ӟ�*�:�.aŐ�ͨ�1~�Z��ڬzt��uk�z�IshJ'��}Hb�vkv����/��fW8>�=�֤6E]V6i[_ȋ{��F�uO#��s�VeS.��q�s���)+G��, %�keΩ3L�G�bv4�ˇ��g���zr7��d�󞦧�u?9ɔQwQr��T�F��h؃�	v�%���wB��T�l4=}�fnF���nzB��)�J+���JG���E�,�4�a� �<�K���Lr�0�Vh�|,��jƆ<�s0E,$���G��;�����c��Z����\3�yia�:��D$��EB9��C�b�0�nYs��h��p�C%#�;��3p4C⺬�Q�d�
�;W�e�bu5�|%]2�DA�.���d��xt�}�7�,��jc���8�ߏg�G�����ŧ�7ֲ���pXİ*n[�ߑ��O%���+≉���H׌Hƚ<����!����v;R![���v���Ԗ�H���&��X���d���G��?-f�/\)��C۷	���nm�-�ހk�!S��U>��4����n��������7�P�}�/�{��Ĺ�K��uQ�W#pD�o�١�l�A'�y2�?�����z � �f���\h���t��w;����]��΄�> �2$���/�|���M^��^U�ޞ�|Т�?���E� �1����?¯��u�<��D�x�ݶ�a^j�WW�����+�y�}a���Q@q��ͱu��1����(	�y����/�E��Cw�����)��%���L-� <$���Y���7�-��n��B�1-�����Q �8��.����
�2d�]a��J���V�G`^o�?��l��a��e�����է��|9r��e`::�8Sb�T���p�=LL=��א�r\�3}�R�_��s�(I`���c���t���b���$��<8��'Z~|<�O�����G V~�7� �a9ݫ�ܸXMj7�?�It0�[F��N�3�J���P��Ի�v�������U���V�w���7���>�V!�����8�U����������� yA�*��&�AXb�t��q���)���-�j�-�n�_�=���@Z��ֆܕ|ޔ�8�ڔv�i��2<�3P-��ʍE�p����3���D�_5�k�� ��P�[]۟E���R��/�A~^����+p����B ���Nqs�2���Oy�|0�U�΁�\�ֹ��_�ó����B>�>��+�{�\�Ճe��+T!*�Ӕ�n�(������Ii^������Зm�u�2z�W��7�U�m���X��3::�*���E�TI�j����J -S�6���m��Rb���.�WP��wʯ��.�p�c�kO`��Zf�DO�w/,Rzxa1޿�(m�1���X'E^��P��R��o^�z�F���      �      x��;�n㸒Ϛ��әH'�,�'}&@21bw�Y`�-1�6��%%{򶿱��_�UE](�V���1��H$EV�uW�:��W��ͣ��q�<���ʣt-�̙�(��=VQ"���܋`œ(�1����,�)6M�q�e�L�le+��<��C�p�����<��a����d�S�{'BŃ�:�n��V�ٓTl�;ǎ��wf�9��ӯsg!Y�d&��e+�D5k��@�e�md���S�YγH&���K`'6t#�~~}9un�PZ5/�f���`S�'�P�
)1�9����z�Y��7N\hzeM�;y%�
����O��|Ó ��f�cC�r��n�o6����z5���M��_���:Gn�&���z�Vr���q��8t�pVB�l.-�޶���{&����J�+�2��{Z�C9�WL�eV��`��DQy��<�[�
�yWׇ�f�'%�Ի�QR��y�Ư�'��^��|e0 G��{L>�������Wаq�^CN���5�>I1��\ 7&��k���w��{�9��k7�Yq:�DgI�:_�WM��|2<z�-����˨�S3�����s>UC=�y��$S2���- 7:�}u3��,`p �D���j�$��	�:e(F�u*�/`!-���2
XL!S-�i
�`�y��d���!�B0)��0�s���D,�D�kq�F��*�I	�s& ���H�&��R�n}˔xJ�G5�T��@�n#Uӡ"Cl�ن�H�"EES��'2ĄYE�l[2��=#,9�1�*�^�tn��M��_�p�$\��T:���eH7�@ҍ;y��&�EPZ#}V�j�	�&
@+�a����u,�H�Pn�:�i
�gH�q)�t*@�ٴ�¨��T��E����C���<i"�5�c�8�c�!�5��
<�	���!`J�A)Jj��y�E)2W��@Y:�ྏ
���Qq0i�y�I���(0rS�f�?�[�-�8�����?p,�B�{����lU)���c'�/_/��GM�Rv��>j�)��L�1�pL����q�2���0��zTe�u@��8Nts�P(�I8�?���h�u����G��F�1$��$8�Z���8�4s�� s�Vx��'%���u�(P���w���ͻLH���@.0n�&'@��g�-�>����َm���w�ص�t�+Am9F�6<��A�D�? Ϲ3�s����w��)8"m��'����Q�ea��Х�FY����BG�:"�3|��:K�<B3G)|�"�9)J�@D�-,�G D"ev�i/d:`E8���,)��R���l�&ó�W�˯�9s�=��G���,��˯7��r��y�7v��/à���ueB5����<h�g�K#���K��s�J#* Z�	��=�9͟D�Zy���o��2!�'�82ox�����ߎ<K.�Үn���콒��d�5�r6���1�l`'���:b��c�{�8 ��D��+u�n3��}�W`0��[G�hC�<19t#@�h�g�܈��@�eb;
]�3y'o�������Qi��"0tEVdK	T��l�����_S"DH8h�!x�0E�U���F�i)�WvREva<�J4��)����>�+J1�7����H��9�ɳ`w�R�N�ѷ���w�S��{�h�R�N���ځB��
�N���ā��%��#�q�>x�t��j��������@�Lm���$b
�H�m��(bY�^���v�@x{h{qoT��o4���Q`�[��Y�t��Zޓn�M�6��Sܙ�j#�8ƌ0"����3�)� 	<�x�$ $0l/
;L��~�?9�����h2�1���4��v�-���*�,Q`)���l�+��r�]�&��9�����D�k�4��D	�.F)�8���������h�qZ!Y(��M��,�"�/Ex�`n�{�ЊWu�<<�����vo���bq|x1��'���/���j�;�r1%�I�J�8��fKwA;vf�p���q��[�@�U�ZG�<
�V
Y�rU��j%x���}zBz�*�sC�׆�"��2�Qb��*:������ݳP�8�[na��v�A��[x�܌gR�<^h^l��x	(qf�1Q�n�̌��!@#���0@{a@�*��_��	���g����������%g�צ�j3 ��0	e,��H����"^�+B����UTz��x�$އ�dt4I���$ I�L�Xק��;(�N�������MM�&.s ص�*4!�8�[]�C��3Q��-'~�좌B ȓ����������r��}��u��� �0��"c��d#��&�\;� H�U"c�u%x�1��~�����Q���Pm'n�(�[~.��ݒ�g��1S:ʔ�=����7��M����~� �)72�D5�����2�d�6�jB?ڷ�%�'����|�w�9��L^G:��e �Ж������X�nz�́%��`KB6U�(�=�1��+��[����l>݃�+�i�@��㌚����Li��G�?-�kV��	�4Cx��<b������E)���������,Z��Z�
V6��Pd�ȶR�a/�r��v5k�-3�aa[E&�)s���.c�s��t��Z[kܡ�&e���O"�`������q�?��GC���G���{�1�\`��V��b���;wMt�v�0���Y�W�*�2P6�,��e�)���w��+�F���;_��$d�:���Ꚕ��Q�E�(�5�Z�~C� ��Njy�P�������Q�Ш��z�LX���lR�:�	-a4�9��(I!83���C�*x�x���*�<9X�Y����;�pD?��M"�b��)+�&:��tt�~S"���_��hp?<�������A��5�f�]&/�B�W\Gq�'z���`����'xW��a��I<S �b��� )���A��Tp���\����{9��A��M7W����&�gĨE��6b�	�¨fI�5Orby�m�Q��VS�r�5���w�M8���)����F���:^C0�6���a�����7��5��{e�.HcQ�l��E��01f�j�FȪrg�tBQb��k�s�&�Hq쀓\�!ؚ3f�^T������o4=�JM�Q��L���|���'�/"+���	<�ly�ՄI�֫8򾊰^�lOO���*-��vI}�(���	~��L�%�Ҽ]�_2DV�E�&kE���a���9/`�(��� ��]��B��yoc���[&��D�ƺ�wG9���Q����$���܁�rZmƭu�>�hw��OB���.Bpò�U�eHE�vQ
`�*�����vӬ(���-�[���R�
������Ҏ��+�g�U�/L|��)�6l�&l��?���6X�X�ց$L���r�$ aj��m�q*�j��h��ᛎ�%�@%�4�z��d<Z��Yʼ,^)\�3bo
ce2ŢdcaqX�qQ�̓�����f�q�w��A�����/���f�Xf
r�Q*Vf<��/�0��<��Gϱ`���)%��"2�ћ#��?�J#���Oz�#�ФUG��b��k�\?�;ׯ	_�T{��D}ڹ#�d��*��OC�R@�K��T������HU�ޱ�����v6Ȏ5)��&`D�
hnP�T�L'�H�E�������լ��x���$�[�μ���������y��'��$Sk��Y�}=t�7{���@��e�C���k�`�:�϶��h�ў�_0�IOT�k���(��u��%��l`�2�Ð�ŖK�Ȕ+��!���6FN��0j�	�.�
Fl�T(;z<7�~ÇVf%�^E"�o�S�V2(`��2{�ʇ���1�nOD'r�9���R��*[l�Ӧ޾\�ۍ�����l�{�h��<�d����o���n����|����g"�5���h��<%�N�k&8��4���N(�a���A̴Ug���h�ZyMZ]`�+�Y�6�ɋ��� �   �9���*ji�ʯ]�`U�R~�WDe�'S^��^II��L��J�����@.d����H�w�}2l������ba>kx(}d��O0	ѵ�{����t�sE_*��mvw���w썴�p�9��o���p#ߠ�h��o��(����_W�zνE#���^UE�E�l�ޟ�UOD<�Դ]Cjj	!���v))�d��������������O�t�eQ      �      x�3��(*c# �4������ DN�      �   �   x�]���0���w�����0!�ċ�� $R}~��Rl;m7�u���`�֡4�ҍX����^��q�.N�ٖ7
oHC&
�X	;��t��!Td*����:��e���,`	ggPLğ=
ߒ%$��v�C?��&�Y�&����|�z��h�c��2-H�$B1�s��zr�H|      �   {   x�3��465�4202�50�54���@<C����i�i�ea��(��#k J8����p��f���($����(�g�d(��d���5�0�k�nd u�!.���qqq �m'�      �     x�u��n�0���S��0J��U�C%���zq`	���l�����[z�5;3�T;xN��'<j{1h��4qZƙ�f"��C^���H�Y���JG�k�eN��L,N�B�0���O��4���H�u���Ҩ*`���	UG&�^QwkPŢ�5xH!����~^��ݳ8���]0_
�d����z� �^Neɜ��fd#~�q�m؂r��=jQyT[˒6X��Z.�����[}^���P?5�m�'����:�A�:�����}'Q��.      �   V   x�3��4@ NC.#N��"��҂��J�����\�ļ������<����T�`�����)[sZZ�Y��0������ ���      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �      x������ � �      �   f  x����N�0��ӧ�՚���P	8�G.ED4�Z	��醓"�ľ|���hL�o�rsX�FD#C���V�(h�&
��@�A�Y�U��w��M$�����y{��n�&E]��ǭ��9K�=��]�v��b�.Y�FDeI����S7u�T��VE7'V����9 rjc+����"O��A92�]����F�WSj�GQ����Ĕ6�ډ�/����|����e�:�Yi:���+m�бv��ͶX��/���r���y�I�����"�8�\�J/`�x ��~�C�^�kX�O9�C�(	�ʉ�L�g�=�5LǏ0y�:�N܄"ye�Ky�p�9͍lg�E�����      �      x������ � �     