# coding: utf-8

"""
    EXACT - API

    API to interact with the EXACT Server  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class Annotation(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'annotation_type': 'int',
        'id': 'int',
        'vector': 'object',
        'verified_by_user': 'str',
        'image': 'int',
        'concealed': 'str',
        'blurred': 'str',
        'last_editor': 'int',
        'user': 'int',
        'deleted': 'bool',
        'description': 'str',
        'unique_identifier': 'str',
        'uploaded_media_files': 'list[int]',
        'annotationversion_set': 'list[int]',
        'meta_data': 'object',
        'time': 'datetime',
        'last_edit_time': 'datetime',
    }

    attribute_map = {
        'annotation_type': 'annotation_type',
        'id': 'id',
        'vector': 'vector',
        'verified_by_user': 'verified_by_user',
        'image': 'image',
        'concealed': 'concealed',
        'blurred': 'blurred',
        'last_editor': 'last_editor',
        'user': 'user',
        'deleted': 'deleted',
        'description': 'description',
        'unique_identifier': 'unique_identifier',
        'uploaded_media_files': 'uploaded_media_files',
        'annotationversion_set': 'annotationversion_set',
        'meta_data': 'meta_data',
        'last_edit_time': 'last_edit_time',
        'time': 'time'
    }

    def __init__(self, annotation_type=None, id=None, vector=None, verified_by_user=None, image=None, concealed=None, blurred=None, last_editor=None, user=None, time=None, last_edit_time=None, deleted=None, description=None, unique_identifier=None, uploaded_media_files=[], meta_data=None, annotationversion_set=[]):  # noqa: E501
        """Annotation - a model defined in Swagger"""  # noqa: E501
        self._annotation_type = None
        self._id = None
        self._vector = None
        self._verified_by_user = None
        self._image = None
        self._concealed = None
        self._blurred = None
        self._last_editor = None
        self._user = None
        self._time = None
        self._last_edit_time = None
        self._deleted = None
        self._description = None
        self._unique_identifier = None
        self._uploaded_media_files = None
        self._annotationversion_set = None
        self._meta_data = None
        self.discriminator = None
        self.annotation_type = annotation_type
        if id is not None:
            self.id = id
        if vector is not None:
            self.vector = vector
        if verified_by_user is not None:
            self.verified_by_user = verified_by_user
        self.image = image
        if concealed is not None:
            self.concealed = concealed
        if blurred is not None:
            self.blurred = blurred
        if last_editor is not None:
            self.last_editor = last_editor
        if user is not None:
            self.user = user
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if unique_identifier is not None:
            self.unique_identifier = unique_identifier
        self.uploaded_media_files = uploaded_media_files
        self.annotationversion_set = annotationversion_set
        if meta_data is not None:
            self.meta_data = meta_data
        if time is not None:
            self.time = time
        if last_edit_time is not None:
            self.last_edit_time = last_edit_time

    @property
    def annotation_type(self):
        """Gets the annotation_type of this Annotation.  # noqa: E501


        :return: The annotation_type of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._annotation_type

    @annotation_type.setter
    def annotation_type(self, annotation_type):
        """Sets the annotation_type of this Annotation.


        :param annotation_type: The annotation_type of this Annotation.  # noqa: E501
        :type: int
        """
        #if annotation_type is None:
        #    raise ValueError("Invalid value for `annotation_type`, must not be `None`")  # noqa: E501

        self._annotation_type = annotation_type

    @property
    def id(self):
        """Gets the id of this Annotation.  # noqa: E501


        :return: The id of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Annotation.


        :param id: The id of this Annotation.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def vector(self):
        """Gets the vector of this Annotation.  # noqa: E501


        :return: The vector of this Annotation.  # noqa: E501
        :rtype: object
        """
        return self._vector

    @vector.setter
    def vector(self, vector):
        """Sets the vector of this Annotation.


        :param vector: The vector of this Annotation.  # noqa: E501
        :type: object
        """

        self._vector = vector

    @property
    def time(self):
        """Gets the time of this Annotation.  # noqa: E501


        :return: The time of this Annotation.  # noqa: E501
        :rtype: object
        """
        return self._time

    @time.setter
    def time(self, time):
        """Sets the time of this Annotation.


        :param time: The time of this Annotation.  # noqa: E501
        :type: object
        """

        self._time = time

    @property
    def last_edit_time(self):
        """Gets the last_edit_time of this Annotation.  # noqa: E501


        :return: The last_edit_time of this Annotation.  # noqa: E501
        :rtype: object
        """
        return self._last_edit_time

    @last_edit_time.setter
    def last_edit_time(self, last_edit_time):
        """Sets the time of this Annotation.


        :param time: The last_edit_time of this Annotation.  # noqa: E501
        :type: object
        """

        self._last_edit_time = last_edit_time

    @property
    def verified_by_user(self):
        """Gets the verified_by_user of this Annotation.  # noqa: E501


        :return: The verified_by_user of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._verified_by_user

    @verified_by_user.setter
    def verified_by_user(self, verified_by_user):
        """Sets the verified_by_user of this Annotation.


        :param verified_by_user: The verified_by_user of this Annotation.  # noqa: E501
        :type: str
        """

        self._verified_by_user = verified_by_user

    @property
    def image(self):
        """Gets the image of this Annotation.  # noqa: E501


        :return: The image of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._image

    @image.setter
    def image(self, image):
        """Sets the image of this Annotation.


        :param image: The image of this Annotation.  # noqa: E501
        :type: int
        """
        #if image is None:
        #    raise ValueError("Invalid value for `image`, must not be `None`")  # noqa: E501

        self._image = image

    @property
    def concealed(self):
        """Gets the concealed of this Annotation.  # noqa: E501


        :return: The concealed of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._concealed

    @concealed.setter
    def concealed(self, concealed):
        """Sets the concealed of this Annotation.


        :param concealed: The concealed of this Annotation.  # noqa: E501
        :type: str
        """

        self._concealed = concealed

    @property
    def blurred(self):
        """Gets the blurred of this Annotation.  # noqa: E501


        :return: The blurred of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._blurred

    @blurred.setter
    def blurred(self, blurred):
        """Sets the blurred of this Annotation.


        :param blurred: The blurred of this Annotation.  # noqa: E501
        :type: str
        """

        self._blurred = blurred

    @property
    def last_editor(self):
        """Gets the last_editor of this Annotation.  # noqa: E501


        :return: The last_editor of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._last_editor

    @last_editor.setter
    def last_editor(self, last_editor):
        """Sets the last_editor of this Annotation.


        :param last_editor: The last_editor of this Annotation.  # noqa: E501
        :type: int
        """

        self._last_editor = last_editor

    @property
    def user(self):
        """Gets the user of this Annotation.  # noqa: E501


        :return: The user of this Annotation.  # noqa: E501
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this Annotation.


        :param user: The user of this Annotation.  # noqa: E501
        :type: int
        """

        self._user = user

    @property
    def deleted(self):
        """Gets the deleted of this Annotation.  # noqa: E501


        :return: The deleted of this Annotation.  # noqa: E501
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this Annotation.


        :param deleted: The deleted of this Annotation.  # noqa: E501
        :type: bool
        """

        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this Annotation.  # noqa: E501


        :return: The description of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Annotation.


        :param description: The description of this Annotation.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def unique_identifier(self):
        """Gets the unique_identifier of this Annotation.  # noqa: E501


        :return: The unique_identifier of this Annotation.  # noqa: E501
        :rtype: str
        """
        return self._unique_identifier

    @unique_identifier.setter
    def unique_identifier(self, unique_identifier):
        """Sets the unique_identifier of this Annotation.


        :param unique_identifier: The unique_identifier of this Annotation.  # noqa: E501
        :type: str
        """

        self._unique_identifier = unique_identifier

    @property
    def uploaded_media_files(self):
        """Gets the uploaded_media_files of this Annotation.  # noqa: E501


        :return: The uploaded_media_files of this Annotation.  # noqa: E501
        :rtype: list[int]
        """
        return self._uploaded_media_files

    @uploaded_media_files.setter
    def uploaded_media_files(self, uploaded_media_files):
        """Sets the uploaded_media_files of this Annotation.


        :param uploaded_media_files: The uploaded_media_files of this Annotation.  # noqa: E501
        :type: list[int]
        """
        #if uploaded_media_files is None:
        #    raise ValueError("Invalid value for `uploaded_media_files`, must not be `None`")  # noqa: E501

        self._uploaded_media_files = uploaded_media_files


    @property
    def annotationversion_set(self):
        """Gets the annotationversion_set of this Annotation.  # noqa: E501


        :return: The annotationversion_set of this Annotation.  # noqa: E501
        :rtype: list[int]
        """
        return self._annotationversion_set

    @annotationversion_set.setter
    def annotationversion_set(self, annotationversion_set):
        """Sets the annotationversion_set of this Annotation.


        :param annotationversion_set: The annotationversion_set of this Annotation.  # noqa: E501
        :type: list[int]
        """
        #if annotationversion_set is None:
        #    raise ValueError("Invalid value for `annotationversion_set`, must not be `None`")  # noqa: E501

        self._annotationversion_set = annotationversion_set

    @property
    def meta_data(self):
        """Gets the meta_data of this Annotation.  # noqa: E501


        :return: The meta_data of this Annotation.  # noqa: E501
        :rtype: object
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this Annotation.


        :param meta_data: The meta_data of this Annotation.  # noqa: E501
        :type: object
        """

        self._meta_data = meta_data

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Annotation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Annotation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
